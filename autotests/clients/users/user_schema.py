from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UserSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id:str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    user: UserSchema

class GetUserResponseSchema(BaseModel):
    user: UserSchema

class UpdateUserRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """
    Описание структуры запроса на обновление пользователя.
    """
    email: EmailStr | None
    lastName: str | None = Field(alias="lastName")
    firstName: str | None = Field(alias="firstName")
    middleName: str | None = Field(alias="middleName")