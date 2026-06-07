from pydantic import BaseModel, Field, HttpUrl, ConfigDict


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """

    filename: str
    directory: str
    upload_file: str

class FileSchema(BaseModel):
    id: str
    url: HttpUrl
    filename: str
    directory: str

class CreateFileResponseSchema(BaseModel):
    file: FileSchema