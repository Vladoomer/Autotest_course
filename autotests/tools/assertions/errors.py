import allure
from clients.erorrs_schema import ValidationErrorSchema, ValidationErrorResponseSchema, InternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length

@allure.step("Check validation error")
def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.message, expected.message, "message")
    assert_equal(actual.input, expected.input, "input")
    assert_equal(actual.context, expected.context, "context")
    assert_equal(actual.location, expected.location, "location")

@allure.step("Check validation error response")
def assert_validation_error_response(actual: ValidationErrorResponseSchema, expected: ValidationErrorResponseSchema):
    assert_length(actual.details, expected.details, "details")

    for index, details in enumerate(expected.details):
        assert_validation_error(actual.details[index], details)

@allure.step("Check internal error response")
def assert_internal_error_response(actual: InternalErrorResponseSchema, expected: InternalErrorResponseSchema):
    """
       Функция для проверки внутренней ошибки. Например, ошибки 404 (File not found).

       :param actual: Фактический ответ API.
       :param expected: Ожидаемый ответ API.
       :raises AssertionError: Если значения полей не совпадают.
       """
    assert_equal(actual.details, expected.details, "details")