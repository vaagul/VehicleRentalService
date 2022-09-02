from abc import ABCMeta, abstractmethod


class BookingInterface(metaclass=ABCMeta):
    @abstractmethod
    def book_vehicle(self, bookings, vehicle_pricing, branches, vehicle_type, start_time, end_time):
        pass

    @abstractmethod
    def get_booking_method(self):
        pass

