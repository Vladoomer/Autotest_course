from http import HTTPStatus

from clients.authentication.authentication_scheme import LoginResponseSchema, LoginRequestSchema
from clients.authentication.authentication_client import get_authentication_client
from clients.users.public_users_client import get_public_users_client
from clients.users.user_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


def test_login():
    public_users_client = get_public_users_client()
    request = CreateUserRequestSchema()
    response_user = public_users_client.create_user(request)

    login_user = LoginRequestSchema(email=request.email, password=request.password)
    auth_user_client = get_authentication_client()
    response_auth = auth_user_client.login_api(login_user)
    login_response_data = LoginResponseSchema.model_validate_json(response_auth.text)


    assert_status_code(response_auth.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)
    validate_json_schema(instance=response_auth.json(), schema=login_response_data.model_json_schema())


