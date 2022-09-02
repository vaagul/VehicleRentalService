from enums.VehicleType import VehicleType
from model.Vehicle import Vehicle
from model.VehiclePricing import VehiclePricing
from service.vehicle.VehicleInterface import VehicleInterface


class VehicleService(VehicleInterface):
    def get_vehicle_type(self):
        return VehicleType.Hatchback  # Defaulting
        # raise Exception("Unknown vehicle type detected")

    def surge_pricing(self):
        pass

    def __init__(self, vehicles=None):
        if vehicles is None:
            vehicles = []
        self.vehicles: [Vehicle] = vehicles

    def validate_and_return_vehicle(self, vehicle_id, vehicle_type, branch_name):
        for vehicle in self.vehicles:
            if vehicle_id == vehicle.vehicle_id:
                raise Exception("Vehicle with id {} already present".format(vehicle_id))
        vehicle = Vehicle(vehicle_id, VehicleType(vehicle_type), branch_name)
        self.vehicles.append(vehicle)
        return vehicle

    def compute_price(self, vehicle: Vehicle, vehicle_pricing: VehiclePricing):
        pass
