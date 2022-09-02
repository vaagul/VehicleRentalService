class Vehicle(object):
    def __init__(self, vehicle_id, vehicle_type, branch_name):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.branch_name = branch_name

    def __repr__(self):
        return "{}:{}:{}".format(self.vehicle_id, self.vehicle_type, self.branch_name)
