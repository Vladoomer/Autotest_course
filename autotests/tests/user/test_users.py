import pytest
from clients.users.public_users_client import PublicUsersClient
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from http import HTTPStatus

from fixtures.users import UserFixture
from tools.tag.epics import AllureEpic
from tools.tag.features import AllureFeature
from tools.tag.stories import AllureStory
from tools.tag.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from clients.users.private_users_client import PrivateUsersClient
from tools.faker import fake
import allure
from allure_commons.types import Severity


@pytest.mark.users
@pytest.mark.regression
@allure.tag(AllureTag.USERS, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.USERS)
class TestUsers:
    @allure.severity(Severity.BLOCKER)
    @pytest.mark.parametrize("email", ["mail.ru", "gmail.com", "example.com"])
    @allure.title("Create user")
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    def test_create_user(self, email: str, public_users_client: PublicUsersClient):
        request = CreateUserRequestSchema(email=fake.email(domain=email))
        response = public_users_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(request, response_data)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    @allure.severity(Severity.CRITICAL)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Get user me")
    def test_get_user_me(
            self,
            private_user_client: PrivateUsersClient,
            function_user: UserFixture
    ):
        request = private_user_client.get_user_me_api()
        response_data = GetUserResponseSchema.model_validate_json(request.text)

        assert_status_code(request.status_code, HTTPStatus.OK)
        assert_get_user_response(response_data, function_user.response)
        validate_json_schema(instance=request.json(), schema=response_data.model_json_schema())
