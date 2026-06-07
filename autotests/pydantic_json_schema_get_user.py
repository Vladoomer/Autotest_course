from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema, CreateUserResponseSchema
from clients.users.private_users_client import get_private_users_client
from faker import Faker
from private_http_builder import AuthenticationUserSchema
from tools.assertions.schema import validate_json_schema
from jsonschema import validate
from clients.users.user_schema import GetUserResponseSchema

public_users_client = get_public_users_client()

fake = Faker()
create_user_request = CreateUserRequestSchema(
    email=str(fake.email()),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

create_user_response = public_users_client.create_user(create_user_request)
user_id = create_user_response.user.id
auth_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_users_client = get_private_users_client(auth_user)
get_api_data = private_users_client.get_user_api(user_id).json()

validate_json_schema(instance=get_api_data, schema=GetUserResponseSchema.model_json_schema())
print(GetUserResponseSchema.model_json_schema())
print(get_api_data)






