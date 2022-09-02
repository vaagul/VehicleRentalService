import threading

from enums.VehicleType import VehicleType
from model.Booking import Booking
from service.booking.BookingFactory import BookingServiceFactory
from service.branch.BranchService import BranchService
from utils.constants.BookingMode import LOWEST_PRICE
from utils.enum_utils import is_valid_vehicle_type
from datetime import datetime


class CarRental(object):
    def __init__(self):
        self.branch_service = BranchService()
        self.bookings: [Booking] = []
        self.booking_lock = threading.Lock()

    def add_branch(self, branch_name):
        self.branch_service.add_branch(branch_name)

    def allocate_price(self, branch_name, vehicle_type, price):
        if is_valid_vehicle_type(vehicle_type):
            self.branch_service.allocate_price(branch_name, vehicle_type, price)
        else:
            raise Exception("Invalid vehicleType {} provided".format(vehicle_type))

    def add_vehicle(self, vehicle_id, vehicle_type, branch_name):
        if is_valid_vehicle_type(vehicle_type):
            self.branch_service.add_vehicle(vehicle_id, vehicle_type, branch_name)

    def _book_vehicle(self, vehicle_type, start_time, end_time, booking_mode=LOWEST_PRICE):
        if is_valid_vehicle_type(vehicle_type):
            booking_service = BookingServiceFactory.get_booking_service(booking_mode)()
            # branches, vehicle_type, start_time, end_time
            with self.booking_lock:
                booking = booking_service.book_vehicle(
                    self.bookings,
                    self.branch_service.vehicle_pricing,
                    self.branch_service.get_branch_info(),
                    vehicle_type,
                    start_time,
                    end_time
                )
                if not booking:
                    raise Exception("No {} available".format(vehicle_type))
                self.bookings.append(booking)

    def book_vehicle(self, vehicle_type, start_time, end_time):
        t = threading.Thread(target=self._book_vehicle, args=(vehicle_type, start_time, end_time))
        t.start()
        t.join()


if __name__ == '__main__':
    car_rental = CarRental()
    car_rental.add_branch("Vihar")
    # car_rental.add_branch("Vihar")
    car_rental.add_branch("Cyber")

    car_rental.allocate_price("Vihar", "Sedan", 100)
    # car_rental.allocate_price("Vihar", "Sedan1", 100)
    car_rental.allocate_price("Vihar", "Hatchback", 80)

    car_rental.allocate_price("Cyber", "Sedan", 200)
    # car_rental.allocate_price("Vihar", "Sedan1", 100)
    car_rental.allocate_price("Cyber", "Hatchback", 50)

    car_rental.add_vehicle("1", "Sedan", "Vihar")
    car_rental.add_vehicle("2", "Sedan", "Cyber")
    car_rental.add_vehicle("3", "Hatchback", "Cyber")

    car_rental.book_vehicle("Sedan", datetime(2020, 2, 29, 10), datetime(2020, 2, 29, 13))
    car_rental.book_vehicle("Sedan", datetime(2020, 2, 29, 14), datetime(2020, 2, 29, 15))
    car_rental.book_vehicle("Sedan", datetime(2020, 2, 29, 14), datetime(2020, 2, 29, 15))
    car_rental.book_vehicle("Sedan", datetime(2020, 2, 29, 14), datetime(2020, 2, 29, 15))

    print(car_rental.bookings)
    print(car_rental.branch_service.get_branch_info())
