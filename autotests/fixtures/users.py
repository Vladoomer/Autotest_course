import pytest
from clients.users.public_users_client import PublicUsersClient, get_public_users_client
from clients.private_http_builder import AuthenticationUserSchema
from pydantic import BaseModel, EmailStr
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema
from clients.users.private_users_client import PrivateUsersClient
from clients.users.private_users_client import get_private_users_client


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    authentication_user: AuthenticationUserSchema

@pytest.fixture
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()

@pytest.fixture
def function_user(public_users_client) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    authentication_user = AuthenticationUserSchema(email=request.email, password=request.password)
    return UserFixture(request=request, response=response, authentication_user= authentication_user)

@pytest.fixture
def private_user_client(function_user) -> PrivateUsersClient:
    return get_private_users_client(function_user.authentication_user)