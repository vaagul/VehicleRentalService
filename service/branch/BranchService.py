from enums.BranchStatus import BranchStatus
from enums.VehicleType import VehicleType
from model.Booking import Booking
from model.Branch import Branch
from model.VehiclePricing import VehiclePricing
from service.branch.BranchInterface import BranchInterface
from service.vehicle.VehicleService import VehicleService
from service.vehicle.VehicleServiceFactory import VehicleServiceFactory


class BranchService(BranchInterface):
    def __init__(self):
        self.branch = {}
        self.vehicle_pricing = []
        self.vehicle_service = VehicleService()

    def __is_valid_branch(self, branch_name):
        return branch_name in self.branch

    def update_branch_status(self, branch_name, branch_status: BranchStatus):
        if self.__is_valid_branch(branch_name):
            self.branch[branch_name].branch_status = branch_status

    def add_branch(self, branch_name):
        if self.__is_valid_branch(branch_name):
            raise Exception("Branch {} already created".format(branch_name))
        self.branch[branch_name] = Branch(branch_name)

    def allocate_price(self, branch_name, vehicle_type, price):
        if self.__is_valid_branch(branch_name):
            self.branch[branch_name].vehicle_pricing[vehicle_type] = price
            self.vehicle_pricing.append(VehiclePricing(branch_name, VehicleType(vehicle_type), price))

    def add_vehicle(self, vehicle_id, vehicle_type, branch_name):
        vehicle_service = VehicleServiceFactory.get_vehicle_service(VehicleType(vehicle_type))
        vehicle_service_obj = vehicle_service(self.vehicle_service.vehicles)
        self.branch[branch_name].vehicles.append(
            vehicle_service_obj.validate_and_return_vehicle(vehicle_id, vehicle_type, branch_name))
        self.vehicle_service.vehicles = vehicle_service_obj.vehicles

    def get_branch_info(self):
        return self.branch

