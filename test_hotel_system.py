import unittest
from hotel_system import Hotel, Room, Amenities, Guest, Booking, Invoice, LoyaltyProgram, GuestServiceRequest, Feedback

class TestHotelSystem(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel("Grand Hotel", "123 Main St", 5.0, "hotel@example.com")
        self.amenities = Amenities(True, True, False, True)
        self.room = Room(101, "Deluxe", 150.0, [self.amenities])
        self.guest = Guest("John Doe", "johndoe@example.com")
        self.booking = Booking(1, self.guest, self.room, "2025-04-01", "2025-04-05", 600.0)
        self.invoice = Invoice(1, self.booking, 600.0)
        self.loyalty_program = LoyaltyProgram(self.guest)
        self.service_request = GuestServiceRequest("Room Cleaning")
        self.feedback = Feedback(5.0, "Great stay!")

    def testHotelInitialization(self):
        self.assertEqual(self.hotel.getName(), "Grand Hotel")
        self.assertEqual(self.hotel.getLocation(), "123 Main St")
        self.assertEqual(self.hotel.getRating(), 5.0)
        self.assertEqual(self.hotel.getContactInfo(), "hotel@example.com")

    def testAmenitiesInitialization(self):
        self.assertTrue(self.amenities.getHasWiFi())
        self.assertTrue(self.amenities.getHasTV())
        self.assertFalse(self.amenities.getHasMinibar())
        self.assertTrue(self.amenities.getHasAirConditioning())

    def testRoomInitialization(self):
        self.assertEqual(self.room.getRoomNumber(), 101)
        self.assertEqual(self.room.getRoomType(), "Deluxe")
        self.assertEqual(self.room.getPricePerNight(), 150.0)
        self.assertEqual(self.room.getAmenities(), [self.amenities])

    def testGuestInitialization(self):
        self.assertEqual(self.guest.getName(), "John Doe")
        self.assertEqual(self.guest.getContactInfo(), "johndoe@example.com")

    def testBookingInitialization(self):
        self.assertEqual(self.booking.getBookingID(), 1)
        self.assertEqual(self.booking.getGuest(), self.guest)
        self.assertEqual(self.booking.getRoom(), self.room)
        self.assertEqual(self.booking.getCheckInDate(), "2025-04-01")
        self.assertEqual(self.booking.getCheckOutDate(), "2025-04-05")
        self.assertEqual(self.booking.getTotalPrice(), 600.0)

    def testInvoiceInitialization(self):
        self.assertEqual(self.invoice.getInvoiceID(), 1)
        self.assertEqual(self.invoice.getBooking(), self.booking)
        self.assertEqual(self.invoice.getAmountDue(), 600.0)

    def testLoyaltyProgramInitialization(self):
        self.assertEqual(self.loyalty_program.getGuest(), self.guest)

    def testGuestServiceRequestInitialization(self):
        self.assertEqual(self.service_request.getServiceType(), "Room Cleaning")
        self.assertEqual(self.service_request.getStatus(), "Pending")

    def testFeedbackInitialization(self):
        self.assertEqual(self.feedback.getRating(), 5.0)
        self.assertEqual(self.feedback.getComment(), "Great stay!")

if __name__ == '__main__':
    unittest.main()
