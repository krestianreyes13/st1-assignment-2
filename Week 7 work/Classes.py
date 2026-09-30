
#This is just what the classes should look like

#Part B
class Patient:
    """A patient owns their ID and name, with no database or UI code."""

    def __init__(self, patient_id: str, name: str, contact_details: str = "") -> None:
        self._patient_id = _required_text(patient_id, "patient_id")
        self._name = _required_name(name)
        if not isinstance(contact_details, str):
            raise TypeError("contact_details must be text")
        else:
            self._contact_details = contact_details.strip()

    def get_patient_id(self) -> str:
        return self._patient_id

    def get_name(self) -> str:
        return self._name

    def update_details(self, name: str) -> None:
        self._name = _required_name(name)

    def get_contact_details(self) -> str:
        return self._contact_details

    def update_contact(self, contact_details: str) -> None:
        if not isinstance(contact_details, str):
            raise TypeError("contact_details must be text")
        else:
            self._contact_details = contact_details.strip()


#Part C
class Practitioner:
    """Stage 4 adds specialty to the Stage 3 practitioner model."""

    def __init__(self, practitioner_id: str, name: str, specialty: str) -> None:
        self._practitioner_id = _required_text(practitioner_id, "practitioner_id")
        self._name = _required_name(name)
        self._specialty = _required_text(specialty, "specialty")

    def get_practitioner_id(self) -> str:
        return self._practitioner_id

    def get_name(self) -> str:
        return self._name

    def get_specialty(self) -> str:
        return self._specialty

    def update_details(self, name: str) -> None:
        self._name = _required_name(name)

    def update_specialty(self, specialty: str) -> None:
        self._specialty = _required_text(specialty, "specialty")

