from clients.courses.courses_client import CoursesClient, get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture
import pytest
from pydantic import BaseModel


class CoursesFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema

@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(function_user.authentication_user)

@pytest.fixture
def function_courses(courses_client: CoursesClient, function_user: UserFixture, function_file: FileFixture) -> CoursesFixture:
    request = CreateCourseRequestSchema(previewFileId=function_file.response.file.id, createdByUserId=function_user.response.user.id)
    response = courses_client.create_course(request=request)
    return CoursesFixture(response=response, request=request)