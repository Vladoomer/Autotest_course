import uuid

from pydantic import BaseModel, Field, EmailStr


class UserScheme(BaseModel):
    id: str = Field(default_factory=lambda : str(uuid.uuid4()))
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    password : str
    last_name : str = Field(alias="lastName")
    first_name : str = Field(alias="firstName")
    middle_name : str = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    user : UserScheme

user_json_model = CreateUserRequestSchema(
    email = "m@gm.com",
    password = "1111",
    lastName="aaa",
    firstName="das",
    middleName="asd"
)

user_user_model = UserScheme(
    email = user_json_model.email,
    lastName=user_json_model.last_name,
    firstName=user_json_model.first_name,
    middleName=user_json_model.middle_name
)

print(CreateUserResponseSchema(user=user_user_model))
