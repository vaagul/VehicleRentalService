import enum
from enums.MetaEnum import MetaEnum


class BranchStatus(enum.Enum,  metaclass=MetaEnum):
    Open = "Open"
    Closed = "Closed"
