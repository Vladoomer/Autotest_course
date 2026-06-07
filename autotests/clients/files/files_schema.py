from pydantic import BaseModel, Field, HttpUrl, ConfigDict
from tools.faker import fake


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """

    filename: str = Field(default_factory=lambda:"{fake.uuid4()}.png")
    directory: str = Field(default="courses")
    upload_file: str

class FileSchema(BaseModel):
    id: str
    url: HttpUrl
    filename: str
    directory: str

class CreateFileResponseSchema(BaseModel):
    file: FileSchema

