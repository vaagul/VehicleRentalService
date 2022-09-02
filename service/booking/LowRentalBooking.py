from enums.VehicleType import VehicleType
from model.Booking import Booking
from service.booking.BookingInterface import BookingInterface


class LowRentalBooking(BookingInterface):
    def book_vehicle(self, bookings, vehicle_pricing, branches, vehicle_type, start_time, end_time):
        unavailable_vehicles, preferred_branch = [], []
        for booking in bookings:
            if start_time <= booking.start_time < end_time or start_time < booking.end_time <= end_time:
                unavailable_vehicles.append(booking.vehicle)
        print(unavailable_vehicles)
        for _vehicle_pricing in vehicle_pricing:
            if _vehicle_pricing.vehicle_type == VehicleType(vehicle_type):
                preferred_branch.append((_vehicle_pricing.branch_name, _vehicle_pricing.price))
        print(preferred_branch)
        preferred_branch = sorted(preferred_branch, key=lambda x: x[1])
        for branch in preferred_branch:
            for vehicle in branches[branch[0]].vehicles:
                if vehicle not in unavailable_vehicles and vehicle.vehicle_type == VehicleType(vehicle_type):
                    diff = end_time - start_time
                    days, seconds = diff.days, diff.seconds
                    hours = days * 24 + seconds // 3600
                    booking = Booking(vehicle, start_time, end_time, "", hours * branch[1])
                    return booking

    def get_booking_method(self):
        return "Lowest rental policy"
