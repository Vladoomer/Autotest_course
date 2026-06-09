from http import HTTPStatus

import pytest
from clients.authentication.authentication_scheme import LoginResponseSchema, LoginRequestSchema
from clients.authentication.authentication_client import get_authentication_client
from clients.users.public_users_client import get_public_users_client
from clients.users.user_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema

@pytest.mark.authentication
@pytest.mark.regression
def test_login(function_user, authentication_client):
    request = LoginRequestSchema(email=function_user.email,password=function_user.password)
    response = authentication_client.login_api(request)
    response_data = LoginResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_login_response(response_data)

    validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())


