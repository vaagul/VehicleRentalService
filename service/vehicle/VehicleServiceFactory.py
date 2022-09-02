from enums.VehicleType import VehicleType
from service.vehicle.SedanVehicleService import SedanVehicleService
from service.vehicle.HatchbackVehicleService import HatchbackVehicleService
from service.vehicle.SuvVehicleService import SuvVehicleService
from service.vehicle.VehicleService import VehicleService


class VehicleServiceFactory:
    service_mapping = {
        VehicleType.Sedan: SedanVehicleService,
        VehicleType.Suv: SuvVehicleService,
        VehicleType.Hatchback: HatchbackVehicleService
    }

    @staticmethod
    def get_vehicle_service(vehicle_type):
        return VehicleServiceFactory.service_mapping.get(vehicle_type, VehicleService)
