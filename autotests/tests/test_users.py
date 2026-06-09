import pytest
from clients.users.public_users_client import get_public_users_client
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from http import HTTPStatus

from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response


@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_users_client):
    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_create_user_response(request, response_data)

    validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(private_user_client, function_user):
    request = private_user_client.get_user_me_api()
    response_data = GetUserResponseSchema.model_validate_json(request.text)

    assert_status_code(request.status_code, HTTPStatus.OK)
    assert_get_user_response(response_data, function_user.response)
    validate_json_schema(instance=request.json(), schema=response_data.model_json_schema())


