from clients.erorrs_schema import InternalErrorResponseSchema
from clients.exercises.exercise_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, ExerciseSchema, \
    GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, GetExercisesResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response


def assert_create_exercise_response(request: CreateExerciseRequestSchema, response: CreateExerciseResponseSchema):
    """
        Проверяем, что ответ на создание упражнения соответсвует запросу

        :param request: Исходный запрос на создание упражнения
        :param response: Ответ API с данными упражнения

        :raises AssertionError: если хотя бы одно поле не совпадает
        """
    assert_equal(request.course_id, response.exercise.course_id, "courseId")
    assert_equal(request.title, response.exercise.title, "title")
    assert_equal(request.order_index, response.exercise.order_index, "orderIndex")
    assert_equal(request.max_score, response.exercise.max_score, "max_score")
    assert_equal(request.min_score, response.exercise.min_score, "min_score")
    assert_equal(request.description, response.exercise.description, "description")
    assert_equal(request.estimated_time, response.exercise.estimated_time, "estimated_time")

def assert_exersice(actual: ExerciseSchema, expected: ExerciseSchema):
    """
            Проверяет, что фактические данные упражнения соответствуют ожидаемым.

            :param actual: Фактические данные упражнения.
            :param expected: Ожидаемые данные упражнения.
            :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.course_id, expected.course_id, "courseId")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.order_index, expected.order_index, "orderIndex")
    assert_equal(actual.max_score, expected.max_score, "maxScore")
    assert_equal(actual.min_score, expected.min_score, "minScore")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimatedTime")
    assert_equal(actual.course_id, expected.course_id, "courseId")




def assert_get_exercise_response(
        get_exercise_response: GetExerciseResponseSchema,
        create_exercise_response: CreateExerciseResponseSchema):
    """
            Проверяет, что ответ на получение упражнения соответствует ответу на его создание.

            :param get_exercise_response: Ответ API при запросе данных упражнения.
            :param create_exercise_response: Ответ API при создании упражнения.
            :raises AssertionError: Если данные файла не совпадают.
    """
    assert_exersice(get_exercise_response.exercise, create_exercise_response.exercise)

def assert_update_exercise_response(
        request: UpdateExerciseRequestSchema,
        response: UpdateExerciseResponseSchema
):
    """
            Проверяем, что ответ на обновление упражнения соответсвует запросу

            :param request: Исходный запрос на обновление упражнения
            :param response: Ответ API с данными упражнения

            :raises AssertionError: если хотя бы одно поле не совпадает
        """
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.order_index, request.order_index, "orderIndex")
    assert_equal(response.exercise.max_score, request.max_score, "maxScore")
    assert_equal(response.exercise.min_score, request.min_score, "minScore")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimatedTime")

def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
            Функция для проверки ошибки, если упражнение не найдено на сервере.

            :param actual: Фактический ответ.
            :raises AssertionError: Если фактический ответ не соответствует ошибке "Exercise not found"
        """
    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)

def assert_get_exercises_response(
        get_exercise_response: GetExercisesResponseSchema,
        create_exercise_response: list[CreateExerciseResponseSchema]
        ):
    """
            Проверяет что ответ на получение списка упражнений соответствует ответам на их создание.

            :param get_exercise_response: Ответ API при запросе списков упражнений.
            :param create_exercise_response: Список API ответов при создании упражнений.
            :raises AssertionError: Если данные упражнений не совпадают.
    """
    assert_length(get_exercise_response.exercises, create_exercise_response, "exercises")

    for index, create_exercise_response in enumerate(create_exercise_response):
        assert_exersice(get_exercise_response.exercises[index], create_exercise_response.exercise)
