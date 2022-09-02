from service.booking.LowRentalBooking import LowRentalBooking
from utils.constants.BookingMode import LOWEST_PRICE


class BookingServiceFactory:
    BookingServices = {
        LOWEST_PRICE: LowRentalBooking
    }

    @staticmethod
    def get_booking_service(mode):
        return BookingServiceFactory.BookingServices.get(mode)
