"""
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "estimatedTime": "string"
  }
}
"""
from pydantic import BaseModel, Field, HttpUrl, EmailStr

class CourseScheme(BaseModel):
    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserScheme = Field(alias="createdByUser")
    preview_file: FileScheme = Field(alias="previewFile")

class UserScheme(BaseModel):
    id: str
    email: EmailStr
    last_name : str = Field(alias="lastName")
    first_name : str = Field(alias="firstName")
    middle_name : str = Field(alias="middleName")

    def get_username(self)->str:
        return f"{self.last_name} {self.first_name}"
class FileScheme(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl

course_default_model = CourseScheme(
    id = "cours_id",
    title = "Playwright",
    maxScore = 100,
    minScore = 10,
    previewFile= FileScheme(
        id = "file_id",
        filename = "file_name",
        directory = "directory",
        url = "http://url.com"
    ),
    createdByUser = UserScheme(
        id = "created_by_user",
        email = "email@gm.com",
        lastName= "last_name",
        firstName= "first_name",
        middleName= "middle_name"
    ),
    description = "Playwright",
    estimatedTime = "1 week"
)

course_json = """
{
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "estimatedTime": "1 week"
}
"""
print(course_default_model)
#course_json_model = CourseScheme.model_validate_json(course_json)
#print(repr(course_json_model.model_dump_json(by_alias=True))) #изменить на альяс