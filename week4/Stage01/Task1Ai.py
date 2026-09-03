# Part D - AI Generated Alternative

appointments = []


def add_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)

    return appointment


print("Welcome to SmartCare Appointment Booking")

patient_name = input("Enter patient name: ")
practitioner_name = input("Enter practitioner name: ")
appointment_time = input("Enter appointment time: ")

new_appointment = add_appointment(
    patient_name,
    practitioner_name,
    appointment_time
)

print("\nAppointment recorded successfully!")

print("Patient:", new_appointment["patient"])
print("Practitioner:", new_appointment["practitioner"])
print("Appointment Time:", new_appointment["time"])
