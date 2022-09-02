from abc import ABCMeta, abstractmethod

from enums.BranchStatus import BranchStatus
from model.Vehicle import Vehicle
from model.VehiclePricing import VehiclePricing


class VehicleInterface(metaclass=ABCMeta):
    @abstractmethod
    def validate_and_return_vehicle(self, vehicle_id, vehicle_type, branch_name):
        pass

    @abstractmethod
    def compute_price(self, vehicle: Vehicle, vehicle_pricing: VehiclePricing):
        pass

    @abstractmethod
    def get_vehicle_type(self):
        pass

    @abstractmethod
    def surge_pricing(self):
        pass

