import enum
from enums.MetaEnum import MetaEnum


class VehicleType(enum.Enum,  metaclass=MetaEnum):
    Sedan = "Sedan"
    Hatchback = "Hatchback"
    Suv = "Suv"
