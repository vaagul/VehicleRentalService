from enums.VehicleType import VehicleType
from service.vehicle.VehicleService import VehicleService


class SuvVehicleService(VehicleService):
    def get_vehicle_type(self):
        return VehicleType.Suv

    def surge_pricing(self):
        pass

