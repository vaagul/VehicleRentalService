from enums.VehicleType import VehicleType
from service.vehicle.VehicleService import VehicleService


class HatchbackVehicleService(VehicleService):
    def get_vehicle_type(self):
        return VehicleType.Hatchback

    def surge_pricing(self):
        pass

