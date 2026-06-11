from http import HTTPStatus

import pytest
from clients.erorrs_schema import InternalErrorResponseSchema
from clients.exercises.exercise_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExercisesQuerySchema, GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, \
    GetExercisesResponseSchema
from clients.exercises.exercises_client import ExerciseClient
from fixtures.courses import CoursesFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_response, assert_get_exercises_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
class TestExercise:
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

    def test_update_exercise(self, exercises_client: ExerciseClient, function_exercises: ExerciseFixture):
        update_request = UpdateExerciseRequestSchema()
        update_response = exercises_client.update_exercise_api(function_exercises.response.exercise.id, update_request)
        update_response_data = UpdateExerciseResponseSchema.model_validate_json(update_response.text)

        assert_status_code(update_response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(update_request, update_response_data)
        validate_json_schema(update_response.json(), GetExerciseResponseSchema.model_json_schema())

    def test_delete_exercise(self, exercises_client: ExerciseClient, function_exercises: ExerciseFixture):
        delete_response = exercises_client.delete_exercise_api(function_exercises.response.exercise.id)
        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        get_response = exercises_client.get_exercise_api(function_exercises.response.exercise.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_response(get_response_data)

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


