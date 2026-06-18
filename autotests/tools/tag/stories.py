from enum import Enum


class AllureStory(str, Enum):
    LOGIN = "Login"

    GET_ENTITIES = "Get entities"
    GET_ENTITY = "Get entity"
    CREATE_ENTITY = "Create entity"
    UPDATE_ENTITY = "Update entity"
    DELETE_ENTITY = "Delete entity"
    VALIDATE_ENTITY = "Validate entity"