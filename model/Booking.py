class Booking(object):
    def __init__(self, vehicle, start_time, end_time, user_id, price):
        self.vehicle = vehicle
        self.start_time = start_time
        self.end_time = end_time
        self.user_id = user_id
        self.total_price = price
        self.booking_status = None

    def __repr__(self):
        return "{}-{}".format(self.vehicle, self.total_price)
