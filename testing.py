from hotel_system import Hotel, Room, Amenities, Guest, Booking, Invoice, LoyaltyProgram, GuestServiceRequest, Feedback

# Create a hotel
hotel = Hotel("Grand Plaza", "123 Main Street, NY", 4.7, "hotel@example.com")

# Create some amenities
amenities = Amenities(True, True, False, True)

# Create rooms and add them to the hotel
room = Room(101, "Deluxe", 200.0, [amenities])
hotel.addRoom(room)

# Create a guest
guest = Guest("John Doe", "john.doe@email.com")

# Create a booking for the guest
booking = Booking(1, guest, room, "2025-04-01", "2025-04-05", 50.0)
hotel.addBooking(booking)

# Generate an invoice for the booking
invoice = Invoice(1, booking, 800.0)
invoice.markAsPaid()

# Register the guest for the loyalty program
loyalty_program = LoyaltyProgram(guest)
loyalty_program.addPoints(150)

# Create a service request
service_request = GuestServiceRequest("Extra towels")
guest.submitServiceRequest(service_request)

# Guest provides feedback
feedback = Feedback(4.5, "Great service, but the Wi-Fi was slow.")
guest.submitFeedback(feedback)

# Display results
print("----- Hotel Details -----")
print(hotel)

print("\n----- Room Details -----")
print(room)

print("\n----- Guest Details -----")
print(guest)

print("\n----- Booking Details -----")
print(booking)

print("\n----- Invoice Details -----")
print(invoice)

print("\n----- Loyalty Program Members -----")
print(loyalty_program)

print("\n----- Service Requests -----")
print(service_request)

print("\n----- Guest Feedback -----")
print(feedback)
