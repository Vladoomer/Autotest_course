from http import HTTPStatus

import allure
import pytest
from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_scheme import LoginResponseSchema, LoginRequestSchema
from fixtures.users import UserFixture
from tools.tag.epics import AllureEpic
from tools.tag.features import AllureFeature
from tools.tag.stories import AllureStory
from tools.tag.tags import AllureTag
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from allure_commons.types import Severity

@pytest.mark.authentication
@pytest.mark.regression
@allure.tag(AllureTag.AUTHENTICATION, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
class TestAuthentication:
    @allure.severity(Severity.BLOCKER)
    @allure.story(AllureStory.LOGIN)
    @allure.title("Login with correct email and password")
    def test_login(self, function_user: UserFixture, authentication_client: AuthenticationClient):
        request = LoginRequestSchema(email=function_user.email, password=function_user.password)
        response = authentication_client.login_api(request)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_data)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
