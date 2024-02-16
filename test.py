class Vehicle:
    def __init__(self, number, car_type, seats):
        self.number = number
        self.car_type = car_type
        self.seats = seats
        self.is_available = True
        self.booked_by = None


def display_available_vehicles(vehicles):
    print("\nAvailable Vehicles:")
    for vehicle in vehicles:
        availability_note = "" if vehicle.is_available else " (Not enough seats)"
        print(f"{vehicle.number}. {vehicle.car_type} - Seats: {vehicle.seats}{availability_note}")


def main():
    # Initialize vehicles
    vehicles = [
        Vehicle(1, "Suzuki Van", 2),
        Vehicle(2, "Toyota Corolla", 4),
        Vehicle(3, "Honda CRV", 4),
        Vehicle(4, "Suzuki Swift", 4),
        Vehicle(5, "Mitsubishi Airtrek", 4),
        Vehicle(6, "Nissan DC Ute", 4),
        Vehicle(7, "Toyota Previa", 7),
        Vehicle(8, "Toyota Hi Ace", 12),
        Vehicle(9, "Toyota Hi Ace", 12),
    ]

    print("Welcome to the University Vehicle Booking System!")

    while True:
        # Step 1: Ask for the number of seats needed
        seats_needed = int(input("\nEnter the number of seats needed (or -1 to stop): "))

        if seats_needed == -1:
            break  # Stop input mode

        # Step 2: Display available vehicles
        display_available_vehicles(vehicles)

        # Step 3: Check and display availability
        available_vehicles = [vehicle for vehicle in vehicles if vehicle.is_available and vehicle.seats >= seats_needed]
        if not available_vehicles:
            print("No available vehicles with the specified number of seats. Please try again.")
            continue

        # Step 4: Ask for the number of the vehicle to be booked
        selected_vehicle_number = int(input("Enter the number of the vehicle to be booked: "))

        # Step 5: Book the vehicle if available
        selected_vehicle = next((vehicle for vehicle in available_vehicles if vehicle.number == selected_vehicle_number), None)
        if selected_vehicle:
            selected_vehicle.is_available = False
            booked_by = input("Enter the name of the person booking the vehicle: ")
            selected_vehicle.booked_by = booked_by
            print(f"\nVehicle {selected_vehicle.number} ({selected_vehicle.car_type}) booked by {booked_by}")
        else:
            print("Invalid selection. Please choose a valid vehicle number.")

    # Display booked vehicles at the end of the day
    print("\nBooked Vehicles at the End of the Day:")
    for vehicle in vehicles:
        if not vehicle.is_available:
            print(f"{vehicle.number}. {vehicle.car_type} - Booked by: {vehicle.booked_by}")


if __name__ == "__main__":
    main()
