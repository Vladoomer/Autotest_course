from clients.api_client import APIClient
from typing import TypedDict

from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.exercises.exercise_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, UpdateExerciseRequestSchema, \
    GetExercisesResponseSchema, GetExerciseResponseSchema, CreateExerciseResponseSchema, UpdateExerciseResponseSchema
from httpx import Response
import allure
from tools.routes import APIRoutes


class ExerciseClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    @allure.step("Get exercises")
    def get_exercises_api(self, exercise_id : GetExercisesQuerySchema) -> Response:
        """
        Метод получения списка упражнений.

        :param exercise_id: Словарь с exercise_id.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(APIRoutes.EXERCISES, params=exercise_id.model_dump(by_alias=True))

    @allure.step("Get exercise by id {exercise_id}")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.EXERCISES}/{exercise_id}")

    @allure.step("Create exercise")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f"{APIRoutes.EXERCISES}", json=request.model_dump(by_alias=True))

    @allure.step("Update exercise by id {exercise_id}")
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema)-> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения
        :param request: Словарь с title, maxScore, minScore, orderIndex,
        description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"{APIRoutes.EXERCISES}/{exercise_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete exercise by id {exercise_id}")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"{APIRoutes.EXERCISES}/{exercise_id}")

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self, query: GetExercisesQuerySchema) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(query)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

def get_exercise_client(user: AuthenticationUserSchema) -> ExerciseClient:
    return ExerciseClient(client=get_private_http_client(user))