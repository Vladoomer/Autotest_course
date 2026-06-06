from pydantic import BaseModel, Field, EmailStr


data = {
    "email": "abs@mail.ru",
    "bio": "this is a bio",
    "age" : 12
}

class UserScheme(BaseModel):
    email : EmailStr
    bio: str | None = Field(min_length=1,max_length=1000)
    age: int = Field(ge=0, le=130)

print(repr(UserScheme(**data)))