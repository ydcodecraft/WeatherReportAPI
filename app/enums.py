# in a larger app, we may create an enum folder that captures enums for different business domain

from enum import Enum

class RequestStatus(str, Enum):
    Success = "Succcess"
    Failure = "Failure"