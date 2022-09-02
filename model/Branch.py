from enums.BranchStatus import BranchStatus
from model.Vehicle import Vehicle


class Branch(object):
    def __init__(self, name):
        self.name = name
        self.address = None
        self.branch_status = BranchStatus.Open
        self.vehicle_pricing = {}  # VehicleType: price
        self.vehicles: [Vehicle] = []

    def __repr__(self):
        # return "\n Branch: {} \n pricing: {} \n vehicles: {}\n".format(self.name, self.vehicle_pricing, self.vehicles)
        return "{}-{}-{}".format(self.name, self.vehicle_pricing, self.vehicles)

