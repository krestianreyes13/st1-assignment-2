from __future__ import annotations

from datetime import datetime


class Patient:
    """Stores details about a patient."""

    def __init__(self, patient_id: str, name: str) -> None:
        self.patient_id = patient_id
        self.name = name

    def update_details(self, name: str) -> None:
        """Validate and update the patient's name."""
        pass


class Practitioner:
    """Stores details about a practitioner."""

    def __init__(self, practitioner_id: str, name: str) -> None:
        self.practitioner_id = practitioner_id
        self.name = name

    def update_details(self, name: str) -> None:
        """Validate and update the practitioner's name."""
        pass


class Appointment:
    """Links one patient and one practitioner to a booking."""

    def __init__(
        self,
        appointment_id: str,
        patient: Patient,
        practitioner: Practitioner,
        scheduled_at: datetime,
        status: str,
    ) -> None:
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.scheduled_at = scheduled_at
        self.status = status

    def reschedule(self, new_time: datetime) -> None:
        """Proposed operation: confirm rescheduling rules first."""
        # A separate booking service will check other bookings for conflicts.
        pass

    def change_status(self, new_status: str) -> None:
        """Change status after the allowed values and rules are confirmed."""
        pass

    def cancel(self) -> None:
        """Provisional operation: confirm cancellation and retention rules."""
        pass