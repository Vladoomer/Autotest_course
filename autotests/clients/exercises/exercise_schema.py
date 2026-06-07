from pydantic import BaseModel, Field, ConfigDict

class ExerciseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class GetExercisesResponseSchema(BaseModel):
    exercises: list[ExerciseSchema]

class GetExerciseResponseSchema(BaseModel):
    exercise: ExerciseSchema

class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений
    """
    courseId : int

class CreateExerciseResponseSchema(BaseModel):
    exercise: ExerciseSchema

class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения
    """
    model_config = ConfigDict(populate_by_name=True)
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class UpdateExerciseResponseSchema(BaseModel):
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """Описание структуры запроса на обновление упражнения"""
    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")