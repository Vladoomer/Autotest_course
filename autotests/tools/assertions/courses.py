import allure
from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, CourseSchema, \
    GetCoursesResponseSchema, CreateCourseResponseSchema, CreateCourseRequestSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user
from tools.logger import get_logger

logger = get_logger("COURSES_ASSERTIONS")
@allure.step("Check update course response")
def assert_update_courses_response(request: UpdateCourseRequestSchema, response: UpdateCourseResponseSchema):
    """
        Проверяем, что ответ на обновление курса соответсвует запросу

        :param request: Исходный запрос на обновление курса
        :param response: Ответ API с данными курса

        :raises AssertionError: если хотя бы одно поле не совпадает
    """
    logger.info("Check update course response")
    assert_equal(response.course.title, request.title, "title")
    assert_equal(response.course.description, request.description, "description")
    assert_equal(response.course.max_score, request.max_score, "max_score")
    assert_equal(response.course.min_score, request.min_score, "min_score")
    assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")

@allure.step("Check course")
def assert_course(actual: CourseSchema, expected: CourseSchema):
    """
            Проверяет, что фактические данные файла соответствуют ожидаемым.

            :param actual: Фактические данные курса.
            :param expected: Ожидаемые данные курса.
            :raises AssertionError: Если хотя бы одно поле не совпадает.
        """
    logger.info("Check course")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")
    assert_equal(actual.description, expected.description, "description")

    assert_file(actual.preview_file, expected.preview_file)
    assert_user(actual.created_by_user, expected.created_by_user)

@allure.step("Check get courses response")
def assert_get_courses_response(
        get_courses_response: GetCoursesResponseSchema,
        create_course_responses: list[CreateCourseResponseSchema]):
    assert_length(get_courses_response.courses, create_course_responses, "courses")
    logger.info("Check get courses response")
    for index, create_course_response in enumerate(create_course_responses):
        assert_course(get_courses_response.courses[index], create_course_response.course)

@allure.step("Check create course response")
def assert_create_courses_response(actual: CreateCourseRequestSchema, expected: CreateCourseResponseSchema):
    """
        Проверяем, что ответ на создание курса соответсвует запросу

        :param actual: Исходный запрос на создание курса
        :param expected: Ответ API с данными курса

    :raises AssertionError: если хотя бы одно поле не совпадает
    """
    logger.info("Check create course response")
    assert_equal(actual.title, expected.course.title, "title")
    assert_equal(actual.description, expected.course.description, "description")
    assert_equal(actual.max_score, expected.course.max_score, "max_score")
    assert_equal(actual.min_score, expected.course.min_score, "min_score")
    assert_equal(actual.estimated_time, expected.course.estimated_time, "estimated_time")
    assert_equal(actual.preview_file_id, expected.course.preview_file.id, "preview_file_id")
    assert_equal(actual.created_by_user_id, expected.course.created_by_user.id, "created_by_user_id")