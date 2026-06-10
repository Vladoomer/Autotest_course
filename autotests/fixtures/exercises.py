from clients.exercises.exercises_client import get_exercise_client, ExerciseClient
from clients.exercises.exercise_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CoursesFixture
from fixtures.users import UserFixture

import pytest
from pydantic import BaseModel


class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema

@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExerciseClient:
    return get_exercise_client(function_user.authentication_user)

@pytest.fixture
def function_exercises(exercises_client: ExerciseClient, function_courses: CoursesFixture) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(courseId=function_courses.response.course.id)
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)

