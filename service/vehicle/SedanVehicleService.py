from enums.VehicleType import VehicleType
from service.vehicle.VehicleService import VehicleService


class SedanVehicleService(VehicleService):
    def get_vehicle_type(self):
        return VehicleType.Sedan

    def surge_pricing(self):
        pass

