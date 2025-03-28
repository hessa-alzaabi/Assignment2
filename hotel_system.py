class Amenities:
    """Represents the amenities available in a hotel room."""

    def __init__(self, hasWiFi: bool, hasTV: bool, hasMinibar: bool, hasAirConditioning: bool):
        """Initializes amenities for a room."""
        try:
            if not isinstance(hasWiFi, bool) or not isinstance(hasTV, bool) or not isinstance(hasMinibar, bool) or not isinstance(hasAirConditioning, bool):
                raise TypeError("Make sure all values have the right type!")

            self.__hasWiFi = hasWiFi
            self.__hasTV = hasTV
            self.__hasMinibar = hasMinibar
            self.__hasAirConditioning = hasAirConditioning

        except TypeError as e:
            print(f"Error: {e}")

    # Getters
    def getHasWiFi(self):
        return self.__hasWiFi

    def getHasTV(self):
        return self.__hasTV

    def getHasMinibar(self):
        return self.__hasMinibar

    def getHasAirConditioning(self):
        return self.__hasAirConditioning

    # Setters
    def setHasWiFi(self, hasWiFi: bool) :
        self.__hasWiFi = hasWiFi

    def setHasTV(self, hasTV: bool):
        self.__hasTV = hasTV

    def setHasMinibar(self, hasMinibar: bool):
        self.__hasMinibar = hasMinibar

    def setHasAirConditioning(self, hasAirConditioning: bool) :
        self.__hasAirConditioning = hasAirConditioning

    # Methods
    def __str__(self):
        """Returns a string representation of the room amenities."""
        return f"Amenities - WiFi: {self.__hasWiFi}, TV: {self.__hasTV}, Mini-Bar: {self.__hasMinibar}, Air Conditioning: {self.__hasAirConditioning}"


class Room:
    """Represents a hotel room with amenities and availability status."""

    def __init__(self, roomNumber: int, roomType: str, pricePerNight: float, amenities: list[Amenities]):
        try:
            if not isinstance(roomNumber, int) or not isinstance(roomType, str) or not isinstance(pricePerNight, float):
                raise TypeError("Make sure all values have the right type!")

            if not isinstance(amenities, list) or not all(isinstance(a, Amenities) for a in amenities):
                raise TypeError("Make sure amenities is a list of Amenities objects!")

            self.__roomNumber = roomNumber
            self.__roomType = roomType
            self.__pricePerNight = pricePerNight
            self.__isAvailable = True
            self.__amenities = amenities  # expects a list of amenities

        except TypeError as e:
            print(f"Error: {e}")

    # Getters
    def getRoomNumber(self):
        return self.__roomNumber

    def getRoomType(self):
        return self.__roomType

    def getPricePerNight(self):
        return self.__pricePerNight

    def isAvailable(self):
        return self.__isAvailable

    def getAmenities(self):
        return self.__amenities

    # Setters
    def setRoomType(self, roomType: str):
        self.__roomType = roomType

    def setPricePerNight(self, pricePerNight: float):
        self.__pricePerNight = pricePerNight

    def setAmenities(self, amenities: list):
        self.__amenities = amenities

    # Methods
    def bookRoom(self):
        """Marks the room as booked."""
        self.__isAvailable = False

    def releaseRoom(self):
        """Marks the room as available again after checkout."""
        self.__isAvailable = True

    def __str__(self):
        return f"Room {self.__roomNumber}: {self.__roomType}, ${self.__pricePerNight}/night, Available: {self.__isAvailable}"


class Hotel:
    """Represents a hotel with rooms, guests, and bookings."""

    def __init__(self, name: str, location: str, rating: float, contactInfo: str):
        try:
            if not isinstance(name, str) or not isinstance(location, str) or not isinstance(rating, float) or not isinstance(contactInfo, str):
                raise TypeError("Make sure all values have the right type!")

            self.__name = name
            self.__location = location
            self.__rating = rating
            self.__contactInfo = contactInfo
            self.__rooms = []  # List of Room objects
            self.__guests = []  # List of Guest objects
            self.__bookings = []  # List of Booking objects

        except TypeError as e:
            print(f"Error: {e}")

    # Getters
    def getName(self):
        return self.__name

    def getLocation(self):
        return self.__location

    def getRating(self):
        return self.__rating

    def getContactInfo(self):
        return self.__contactInfo

    def getRooms(self):
        return self.__rooms

    def getGuests(self):
        return self.__guests

    def getBookings(self):
        return self.__bookings

    # Setters
    def setName(self, name: str):
        self.__name = name

    def setLocation(self, location: str):
        self.__location = location

    def setRating(self, rating: float):
        self.__rating = rating

    def setContactInfo(self, contactInfo: str):
        self.__contactInfo = contactInfo

    # Methods
    def addRoom(self, room):
        """Adds a room to the hotel's room list."""
        try:
            if not isinstance(room, Room):
                raise TypeError("Invalid room object.")

            for r in self.__rooms:
                if r.getRoomNumber() == room.getRoomNumber():
                    raise ValueError(f"Room {room.getRoomNumber()} already exists.")

            self.__rooms.append(room)

        except TypeError as e:
            print(f"Error: {e}")

    def addGuest(self, guest):
        """Adds a guest to the hotel's guest list."""
        try:
            if not isinstance(guest, Guest):
                raise TypeError("Invalid guest object.")

            self.__guests.append(guest)

        except TypeError as e:
            print(f"Error: {e}")

    def addBooking(self, booking):
        """Adds a booking to the hotel's booking list."""
        try:
            if not isinstance(booking, Booking):
                raise TypeError("Invalid booking object.")

            self.__bookings.append(booking)

        except TypeError as e:
            print(f"Error: {e}")

    def __str__(self):
        """Returns a string representation of the hotel."""
        return f"{self.__name}, {self.__location}, Rating: {self.__rating}, Contact: {self.__contactInfo}"


class GuestServiceRequest:
    """Represents a guest's request for additional hotel services."""

    def __init__(self, serviceType: str):
        """Initializes a service request with necessary details."""
        try:
            if not isinstance(serviceType, str):
                raise TypeError("Make sure all values have the right type!")

            self.__serviceType = serviceType
            self.__status = "Pending"  # Default status is "Pending"

        except TypeError as e:
            print(f"Error: {e}")

    # Getters
    def getServiceType(self):
        return self.__serviceType

    def getStatus(self):
        return self.__status

    # Setters
    def setServiceType(self, serviceType: str):
        self.__serviceType = serviceType

    def setStatus(self, status: str):
        """Updates the request status (e.g., 'Pending', 'Completed', 'Cancelled')."""
        validStatuses = ["Pending", "Completed", "Cancelled"]
        if status in validStatuses:
            self.__status = status

    # Methods
    def markAsCompleted(self):
        """Marks the service request as completed."""
        self.__status = "Completed"

    def cancelRequest(self):
        """Cancels the service request."""
        self.__status = "Cancelled"

    def __str__(self):
        """Returns a string representation of the service request."""
        return f"Request- Service: {self.__serviceType} | Status: {self.__status}"


class Feedback:
    """Represents feedback provided by a guest after their stay."""

    def __init__(self, rating: float, comment: str):
        """Initializes a feedback entry with a guest, rating, and comment."""
        try:
            if not isinstance(rating, float) or not isinstance(comment, str):
                raise TypeError("Make sure all values have the right type!")

            self.__rating = rating  # Rating should be between 1.0 and 5.0
            self.__comment = comment

        except TypeError as e:
            print(f"Error: {e}")

    # Getters
    def getRating(self):
        return self.__rating

    def getComment(self):
        return self.__comment

    # Setters
    def setRating(self, rating: float):
        """Sets the guest's rating (ensures it is between 1.0 and 5.0)."""
        if 1.0 <= rating <= 5.0:
            self.__rating = rating

    def setComment(self, comment: str):
        """Updates the guest's comment."""
        self.__comment = comment

    # Methods
    def __str__(self) :
        """Returns a string representation of the feedback."""
        return f"Feedback:- Rating: {self.__rating}/5.0 | Comment: {self.__comment}"


class Guest:
    """Represents a hotel guest with personal details and reservation history."""

    def __init__(self, name: str, contactInfo: str):
        """Initializes a guest with name, contact info, and loyalty points."""
        try:
            if not isinstance(name, str) or not isinstance(contactInfo, str):
                raise TypeError("Make sure all values have the right type!")

            self.__name = name
            self.__contactInfo = contactInfo
            self.__loyaltyPoints = 0
            self.__reservations = []  # List of Booking objects
            self.__serviceRequests = []  # List of GuestServiceRequest objects
            self.__feedbacks = []  # List of Feedback objects

        except TypeError as e:
            print(f"Error: {e}")

    # Getters
    def getName(self) :
        return self.__name

    def getContactInfo(self):
        return self.__contactInfo

    def getLoyaltyPoints(self):
        return self.__loyaltyPoints

    def getReservations(self):
        return self.__reservations

    def getServiceRequests(self):
        return self.__serviceRequests

    def getFeedbacks(self):
        return self.__feedbacks

    # Setters
    def setName(self, name: str):
        self.__name = name

    def setContactInfo(self, contactInfo: str):
        self.__contactInfo = contactInfo

    def setLoyaltyPoints(self, points: int):
        if points >= 0:
            self.__loyaltyPoints = points

    # Methods
    def addReservation(self, booking):
        """Adds a booking to the guest's reservation history."""
        try:
            if not isinstance(booking, Booking):
                raise TypeError("Invalid booking object.")

            self.__reservations.append(booking)

        except TypeError as e:
            print(f"Error: {e}")

    def redeemLoyaltyPoints(self, points: int):
        """Redeems loyalty points if the guest has enough."""
        try:
            if not isinstance(points, int):
                raise TypeError("Points must be in integer form.")

            if points <= self.__loyaltyPoints:
                self.__loyaltyPoints -= points
                return True

            return False

        except TypeError as e:
            print(f"Error: {e}")

    def submitServiceRequest(self, request: GuestServiceRequest):
        """Submits a guest service request."""
        try:
            if not isinstance(request, GuestServiceRequest):
                raise TypeError("Request must be of type GuestServiceRequest.")

            self.__serviceRequests.append(request)

        except TypeError as e:
            print(f"Error: {e}")

    def submitFeedback(self, feedback: Feedback):
        """Submits feedback after a stay."""
        try:
            if not isinstance(feedback, Feedback):
                raise TypeError("Feedback must be of type Feedback.")

            self.__feedbacks.append(feedback)

        except TypeError as e:
            print(f"Error: {e}")

    def __str__(self):
        """Returns a string representation of the guest."""
        return f"Guest: {self.__name}, Contact: {self.__contactInfo}, Points: {self.__loyaltyPoints}"


class Booking:
    """Represents a booking made by a guest for a hotel room."""

    def __init__(self, bookingID: int, guest: Guest, room: Room, checkInDate: str, checkOutDate: str, totalPrice: float):
        """Initializes a booking with necessary details."""
        try:
            if not isinstance(bookingID, int) or not isinstance(guest, Guest) or not isinstance(room, Room) or not isinstance(checkInDate, str) or not isinstance(checkOutDate, str) or not isinstance(totalPrice, float):
                raise TypeError("Make sure all values have the right type!")

            self.__bookingID = bookingID
            self.__guest = guest
            self.__room = room
            self.__checkInDate = checkInDate
            self.__checkOutDate = checkOutDate
            self.__totalPrice = totalPrice
            self.__isActive = True  # Booking is active when created
            self.__room.bookRoom() # Room is booked

        except TypeError as e:
            print(f"Error: {e}")

    # Getters
    def getBookingID(self):
        return self.__bookingID

    def getGuest(self):
        return self.__guest

    def getRoom(self):
        return self.__room

    def getCheckInDate(self):
        return self.__checkInDate

    def getCheckOutDate(self):
        return self.__checkOutDate

    def getTotalPrice(self):
        return self.__totalPrice

    def isActive(self):
        return self.__isActive

    # Setters
    def setCheckInDate(self, checkInDate: str):
        self.__checkInDate = checkInDate

    def setCheckOutDate(self, checkOutDate: str):
        self.__checkOutDate = checkOutDate

    def setTotalPrice(self, totalPrice: float):
        self.__totalPrice = totalPrice

    # Methods
    def cancelBooking(self):
        """Cancels the booking and releases the room."""
        if self.__isActive:
            self.__isActive = False
            self.__room.releaseRoom()

    def __str__(self) -> str:
        """Returns a string representation of the booking."""
        status = "Active" if self.__isActive else "Cancelled"
        return f"Booking {self.__bookingID}: {self.__guest.getName()} | Room {self.__room.getRoomNumber()} | {self.__checkInDate} to {self.__checkOutDate} | {status}"


class Invoice:
    """Represents an invoice for a booking, detailing charges and payments."""

    def __init__(self, invoiceID: int, booking: Booking, amountDue: float):
        """Initializes an invoice with necessary details."""
        try:
            if not isinstance(invoiceID, int) or not isinstance(booking, Booking) or not isinstance(amountDue, float):
                raise TypeError("Make sure all values have the right type!")

            self.__invoiceID = invoiceID
            self.__booking = booking
            self.__amountDue = amountDue
            self.__paymentStatus = "Pending"  # Default status is "Pending"

        except TypeError as e:
            print(f"Error: {e}")

    # Getters
    def getInvoiceID(self):
        return self.__invoiceID

    def getBooking(self):
        return self.__booking

    def getAmountDue(self):
        return self.__amountDue

    def getPaymentStatus(self):
        return self.__paymentStatus

    # Setters
    def setAmountDue(self, amountDue: float) :
        self.__amountDue = amountDue

    def setPaymentStatus(self, paymentStatus: str) :
        """Updates the payment status (e.g., 'Paid', 'Pending', 'Cancelled')."""
        validStatuses = ["Paid", "Pending", "Cancelled"]
        if paymentStatus in validStatuses:
            self.__paymentStatus = paymentStatus

    # Methods
    def markAsPaid(self) :
        """Marks the invoice as paid."""
        self.__paymentStatus = "Paid"

    def __str__(self):
        """Returns a string representation of the invoice."""
        return f"Invoice {self.__invoiceID}: Booking {self.__booking.getBookingID()} | Amount Due: ${self.__amountDue:.2f} | Status: {self.__paymentStatus}"


class LoyaltyProgram:
    """Represents a hotel's loyalty program for returning guests."""

    def __init__(self, guest: Guest):
        """Initializes a loyalty program with a guest and their reward points."""
        try:
            if not isinstance(guest, Guest):
                raise TypeError("Make sure all values have the right type!")

            self.__guest = guest
            self.__points = 0

        except TypeError as e:
            print(f"Error: {e}")

    # Getters
    def getGuest(self):
        return self.__guest

    def getPoints(self) :
        return self.__points

    # Setters
    def setPoints(self, points: int):
        """Sets the guest's points (ensures non-negative values)."""
        if points >= 0:
            self.__points = points

    # Methods
    def addPoints(self, amount: int) :
        """Adds points to the guest's loyalty balance."""
        try:
            if not isinstance(amount, int):
                raise TypeError("Amount of points must be an integer!")

            if amount > 0:
                self.__points += amount

        except TypeError as e:
            print(f"Error: {e}")

    def redeemPoints(self, amount: int) :
        """Redeems points for discounts if enough points are available."""
        try:
            if not isinstance(amount, int):
                raise TypeError("Amount of points must be an integer!")

            if 0 < amount <= self.__points:
                self.__points -= amount
                return True  # Successful redemption

            return False  # Not enough points

        except TypeError as e:
            print(f"Error: {e}")

    def __str__(self) :
        """Returns a string representation of the loyalty program details."""
        return f"{self.__guest.getName()} - Loyalty Points: {self.__points}"
