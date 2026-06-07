from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema, CreateUserResponseSchema
from tools.faker import fake
from tools.assertions.schema import validate_json_schema
from jsonschema import validate
public_users_client = get_public_users_client()


create_user_request = CreateUserRequestSchema(
    email=str(fake.email()),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_json = create_user_response.json()
create_user_response_schema = CreateUserResponseSchema.model_json_schema()

validate_json_schema(create_user_response_json, create_user_response_schema)



