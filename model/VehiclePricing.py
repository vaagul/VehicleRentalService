class VehiclePricing(object):
    def __init__(self, branch_name, vehicle_type, price):
        self.branch_name = branch_name
        self.vehicle_type = vehicle_type
        self.price = price

    def __repr__(self):
        return "{}-{}-{}".format(self.branch_name, self.vehicle_type, self.price)
