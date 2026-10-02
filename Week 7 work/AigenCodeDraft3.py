from datetime import datetime
from enum import Enum


def required_text(value: str, field: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f"{field} must be text")
    elif value.strip() == "":
        raise ValueError(f"{field} must not be blank")
    else:
        return value.strip()


def required_name(value: str) -> str:
    value = required_text(value, "Name")
    has_letter = False

    for character in value:
        if character.isalpha():
            has_letter = True

    if has_letter:
        return value
    else:
        raise ValueError("Name must contain at least one letter")


class Patient:
    def __init__(self, patient_id: str, name: str,
                 contact_details: str = "") -> None:
        self._patient_id = required_text(patient_id, "patient_id")
        self._name = required_name(name)

        if not isinstance(contact_details, str):
            raise TypeError("contact_details must be text")
        else:
            self._contact_details = contact_details.strip()

    def get_patient_id(self) -> str:
        return self._patient_id

    def get_name(self) -> str:
        return self._name

    def update_details(self, name: str) -> None:
        self._name = required_name(name)

    def get_contact_details(self) -> str:
        return self._contact_details

    def update_contact(self, contact_details: str) -> None:
        if not isinstance(contact_details, str):
            raise TypeError("contact_details must be text")
        else:
            self._contact_details = contact_details.strip()


class Practitioner:
    def __init__(self, practitioner_id: str, name: str,
                 specialty: str) -> None:
        self._practitioner_id = required_text(
            practitioner_id, "practitioner_id"
        )
        self._name = required_name(name)
        self._specialty = required_text(specialty, "specialty")

    def get_practitioner_id(self) -> str:
        return self._practitioner_id

    def get_name(self) -> str:
        return self._name

    def get_specialty(self) -> str:
        return self._specialty

    def update_details(self, name: str) -> None:
        self._name = required_name(name)

    def update_specialty(self, specialty: str) -> None:
        self._specialty = required_text(specialty, "specialty")


class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"
    COMPLETED = "completed"


class InvalidStatusTransitionError(ValueError):
    pass


class Appointment:
    def __init__(self, appointment_id: str, patient: Patient,
                 practitioner: Practitioner,
                 scheduled_at: datetime) -> None:
        self._appointment_id = required_text(
            appointment_id, "appointment_id"
        )

        if not isinstance(patient, Patient):
            raise TypeError("patient must be a Patient")

        if not isinstance(practitioner, Practitioner):
            raise TypeError("practitioner must be a Practitioner")

        if not isinstance(scheduled_at, datetime):
            raise TypeError("scheduled_at must be a datetime")

        self._patient = patient
        self._practitioner = practitioner
        self._scheduled_at = scheduled_at
        self._status = AppointmentStatus.SCHEDULED

    def get_appointment_id(self) -> str:
        return self._appointment_id

    def get_patient(self) -> Patient:
        return self._patient

    def get_practitioner(self) -> Practitioner:
        return self._practitioner

    def get_scheduled_at(self) -> datetime:
        return self._scheduled_at

    def get_status(self) -> AppointmentStatus:
        return self._status

    def change_status(self, new_status: AppointmentStatus) -> None:
        if not isinstance(new_status, AppointmentStatus):
            raise TypeError("Use an AppointmentStatus value")
        elif self._status == AppointmentStatus.CANCELLED:
            raise InvalidStatusTransitionError("Already cancelled")
        elif self._status == AppointmentStatus.COMPLETED:
            raise InvalidStatusTransitionError("Already completed")
        else:
            self._status = new_status

    def cancel(self) -> None:
        self.change_status(AppointmentStatus.CANCELLED)

    def complete(self) -> None:
        self.change_status(AppointmentStatus.COMPLETED)

    def reschedule(self, new_time: datetime) -> None:
        if not isinstance(new_time, datetime):
            raise TypeError("The new time must be a datetime")
        else:
            self._scheduled_at = new_time

    def send_reminder(self) -> str:
        return "Reminder sent"


def ask_text(prompt: str, is_name: bool = False) -> str:
    while True:
        value = input(prompt)

        try:
            if is_name:
                value = required_name(value)
            else:
                value = required_text(value, "This field")
        except (TypeError, ValueError) as error:
            print(error)
            print("Please try again.\n")
        else:
            return value


def ask_time() -> datetime:
    while True:
        value = input("Date and time (YYYY-MM-DD HH:MM): ")

        try:
            booking_time = datetime.strptime(
                value.strip(), "%Y-%m-%d %H:%M"
            )
        except ValueError:
            print("Please try again, for example: 2026-10-05 09:30\n")
        else:
            return booking_time

def main() -> None:
    print("Create a patient")
    patient_id = ask_text("Patient ID: ")
    patient_name = ask_text("Patient name: ", is_name=True)
    contact = input("Contact details (optional): ")
    patient = Patient(patient_id, patient_name, contact)

    print("\nCreate a practitioner")
    practitioner_id = ask_text("Practitioner ID: ")
    practitioner_name = ask_text("Practitioner name: ", is_name=True)
    specialty = ask_text("Specialty: ")
    practitioner = Practitioner(
        practitioner_id, practitioner_name, specialty
    )

    print("\nCreate an appointment")
    appointment_id = ask_text("Appointment ID: ")
    booking_time = ask_time()
    appointment = Appointment(
        appointment_id, patient, practitioner, booking_time
    )
    print("Appointment created successfully.")

    while True:
        print("\n1. Show appointment")
        print("2. Update patient name")
        print("3. Update practitioner name")
        print("4. Reschedule appointment")
        print("5. Cancel appointment")
        print("6. Complete appointment")
        print("7. Exit")
        choice = input("Choose 1 to 7: ").strip()

        try:
            if choice == "1":
                print("ID:", appointment.get_appointment_id())
                print("Patient:", patient.get_name())
                print("Contact:", patient.get_contact_details())
                print("Practitioner:", practitioner.get_name())
                print("Specialty:", practitioner.get_specialty())
                print("Time:", appointment.get_scheduled_at())
                print("Status:", appointment.get_status().value)
            elif choice == "2":
                new_name = ask_text("New patient name: ", is_name=True)
                patient.update_details(new_name)
                print("Name updated.")
            elif choice == "3":
                new_name = ask_text("New practitioner name: ", is_name=True)
                practitioner.update_details(new_name)
                print("Name updated.")
            elif choice == "4":
                new_time = ask_time()
                appointment.reschedule(new_time)
                print("Appointment rescheduled.")
            elif choice == "5":
                appointment.cancel()
                print("Appointment cancelled.")
            elif choice == "6":
                appointment.complete()
                print("Appointment completed.")
            elif choice == "7":
                print("Goodbye.")
                break
            else:
                print("Please try again. Choose a number from 1 to 7.")
        except (TypeError, ValueError) as error:
            print(error)
            print("Please choose another action.")

if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nInput ended. Goodbye.")
