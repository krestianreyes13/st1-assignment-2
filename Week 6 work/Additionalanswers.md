# Stage 3 – Additional Questions and Answers

## Note

The shared questions are answered in the completed lab PDF. This file answers the remaining questions and adds explanations where the PDF only partly covers them.

## Should Database be a class?

Database should not be a class in this domain model. It is a tool for storing information, rather than a person or booking represented by the system. Storage can be handled separately when the system is developed.

## Patient to Appointment: which relationship and why?

Patient and Appointment have an association, which means they are linked.

One patient can have zero or many appointments. Each appointment belongs to one patient.

I chose this relationship because an appointment refers to a patient, but neither is a type of the other. The requirements do not say that deleting a patient should automatically delete their appointments, so I did not use composition.

## Should Appointment inherit from Patient?

No. Inheritance means one class is a type of another class. An appointment is not a type of patient.

Instead, Appointment stores a reference to the Patient attending the booking.

## Critique the AI proposal: PatientManager

A separate PatientManager is not needed in the current domain model. Patient can hold and update its own details.

Tasks involving a collection of patients, such as searching, can be handled separately when the application is developed.

## Critique the AI proposal: PractitionerManager

A separate PractitionerManager is not needed in the current domain model. Practitioner can hold and update its own details.

Tasks such as finding all bookings for a practitioner involve several records and can be handled separately.

## Critique the AI proposal: ClinicController

ClinicController is not needed in the current domain model. The requirements do not give it a clear responsibility.

A controller may help coordinate actions in the working application later, but it does not need to be included as a core domain class.


### Responsibility allocation

Each class looks after its own information.

Patient and Practitioner manage their own details. Appointment manages its booking time, status and links to the patient and practitioner.

Checking for booking conflicts needs information from other appointments. This should be handled by a separate booking service when the application is developed.

### Key relationships

Each appointment links to one patient and one practitioner. Both patients and practitioners can have zero or many appointments.

These links avoid copying patient and practitioner details into every booking. They also make information easier to update.

### Details requiring confirmation

The allowed statuses, exact booking conflict rules and cancellation rules still need confirmation. Rescheduling and cancellation operations are proposed and should be confirmed before they are fully implemented.