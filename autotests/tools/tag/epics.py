from enum import Enum

class AllureEpic(str, Enum):
    LMS = "LMS Service"
    STUDENT = "STUDENT Service"
    ADMINISTRATION = "ADMINISTRATION Service"