"""Vehicle Booking Function Program
Created the program using definitive functions, and
used 'while' loops for simpler use and clearer understanding."""


def initialize_vehicles():
    return [
        {"number": 1, "car_type": "Suzuki Van", "seats": 2, "is_available": True, "booked_by": None},
        {"number": 2, "car_type": "Toyota Corolla", "seats": 4, "is_available": True, "booked_by": None},
        {"number": 3, "car_type": "Honda CRV", "seats": 4, "is_available": True, "booked_by": None},
        {"number": 4, "car_type": "Suzuki Swift", "seats": 4, "is_available": True, "booked_by": None},
        {"number": 5, "car_type": "Mitsubishi Airtrek", "seats": 4, "is_available": True, "booked_by": None},
        {"number": 6, "car_type": "Nissan DC Ute", "seats": 4, "is_available": True, "booked_by": None},
        {"number": 7, "car_type": "Toyota Previa", "seats": 7, "is_available": True, "booked_by": None},
        {"number": 8, "car_type": "Toyota Hi Ace", "seats": 12, "is_available": True, "booked_by": None},
        {"number": 9, "car_type": "Toyota Hi Ace", "seats": 12, "is_available": True, "booked_by": None},
    ]


def display_available_vehicles(vehicles):
    print("\nAvailable Vehicles:")
    for vehicle in vehicles:
        availability_note = "" if vehicle["is_available"] else " (Not enough seats)"
        print(f"{vehicle['number']}. {vehicle['car_type']} - Seats: {vehicle['seats']}{availability_note}")


def book_vehicle(vehicles, selected_vehicle_number, booked_by):
    selected_vehicle = next((vehicle for vehicle in vehicles if vehicle["number"] == selected_vehicle_number), None)
    if selected_vehicle and selected_vehicle["is_available"]:
        selected_vehicle["is_available"] = False
        selected_vehicle["booked_by"] = booked_by
        print(f"\nVehicle {selected_vehicle['number']} ({selected_vehicle['car_type']}) booked by {booked_by}")
        print(f"Thank you for using the Vehicle Booking Function!"
              f"Goodbye!")
        return True
    else:
        print("Invalid selection or the vehicle is not available. Please choose a valid vehicle number.")
        return False


def main():
    vehicles = initialize_vehicles()

    print("Welcome to the University Vehicle Booking System!")

    while True:
        seats_needed = int(input("\nEnter the number of seats needed (or -1 to stop): "))

        if seats_needed == -1:
            break  # Stop input mode

        display_available_vehicles(vehicles)

        available_vehicles = [vehicle for vehicle in vehicles if vehicle["is_available"]
                              and vehicle["seats"] >= seats_needed]
        if not available_vehicles:
            print("No available vehicles with the specified number of seats. Please try again.")
            continue

        selected_vehicle_number = int(input("Enter the number of the vehicle to be booked: "))
        booked_by = input("Enter the name of the person booking the vehicle: ")

        if not book_vehicle(vehicles, selected_vehicle_number, booked_by):
            continue

    print("\nBooked Vehicles at the End of the Day:")
    for vehicle in vehicles:
        if not vehicle["is_available"]:
            print(f"{vehicle['number']}. {vehicle['car_type']} - Booked by: {vehicle['booked_by']}")


if __name__ == "__main__":
    main()
