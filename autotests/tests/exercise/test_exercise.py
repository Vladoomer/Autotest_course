from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity
from clients.erorrs_schema import InternalErrorResponseSchema
from clients.exercises.exercise_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExercisesQuerySchema, GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, \
    GetExercisesResponseSchema
from clients.exercises.exercises_client import ExerciseClient
from fixtures.courses import CoursesFixture
from fixtures.exercises import ExerciseFixture
from tools.tag.epics import AllureEpic
from tools.tag.features import AllureFeature
from tools.tag.stories import AllureStory
from tools.tag.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_response, assert_get_exercises_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(AllureTag.EXERCISES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.EXERCISES)
class TestExercise:
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.title("Create exercise")
    @allure.severity(Severity.BLOCKER)
    def test_create_exercise(
            self,
            exercises_client: ExerciseClient,
            function_exercises: ExerciseFixture,
            function_courses: CoursesFixture):
        request = CreateExerciseRequestSchema(courseId=function_courses.response.course.id)
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.GET_ENTITY)
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.title("Get exercise")
    @allure.severity(Severity.BLOCKER)
    def test_get_exercise(
            self,
            exercises_client: ExerciseClient,
            function_exercises: ExerciseFixture
    ):
        response = exercises_client.get_exercise_api(function_exercises.response.exercise.id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(response_data, function_exercises.response)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.title("Update exercise")
    @allure.severity(Severity.CRITICAL)
    def test_update_exercise(self, exercises_client: ExerciseClient, function_exercises: ExerciseFixture):
        update_request = UpdateExerciseRequestSchema()
        update_response = exercises_client.update_exercise_api(function_exercises.response.exercise.id, update_request)
        update_response_data = UpdateExerciseResponseSchema.model_validate_json(update_response.text)

        assert_status_code(update_response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(update_request, update_response_data)
        validate_json_schema(update_response.json(), GetExerciseResponseSchema.model_json_schema())

    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.title("Delete exercise")
    @allure.severity(Severity.CRITICAL)
    def test_delete_exercise(self, exercises_client: ExerciseClient, function_exercises: ExerciseFixture):
        delete_response = exercises_client.delete_exercise_api(function_exercises.response.exercise.id)
        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        get_response = exercises_client.get_exercise_api(function_exercises.response.exercise.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_response(get_response_data)

    @allure.story(AllureStory.GET_ENTITIES)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("Get exercises")
    @allure.severity(Severity.BLOCKER)
    def test_get_exercises(
            self,
            exercises_client: ExerciseClient,
            function_exercises: ExerciseFixture,
            function_courses: CoursesFixture
        ):
        query = GetExercisesQuerySchema(course_id=function_courses.response.course.id)

        response = exercises_client.get_exercises_api(query)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercises_response(response_data, [function_exercises.response])

        validate_json_schema(response.json(), GetExercisesResponseSchema.model_json_schema())


