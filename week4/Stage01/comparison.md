# Part C - Use AI as Tutor

## 1. Explain What the Code Does

The code creates an empty list called `appointments` which is used to store appointment information.

The `book_appointment()` function takes three pieces of information:

- Patient name
- Practitioner name
- Appointment time

The function checks whether the patient name is empty. If it is empty, it displays an error using:

    if not patient_name:
        raise ValueError("Patient name cannot be empty")

If the patient name is provided, the function creates a dictionary containing the patient name, practitioner name and appointment time.

The appointment is then added to the `appointments` list.

The `display_appointments()` function displays all appointments that have been stored. If there are no appointments, it displays `"No appointments recorded."`

## 2. Three Limitations

1. **Only the patient name is checked.**  
   The practitioner name and appointment time could be empty or invalid.

2. **Double bookings are not prevented.**  
   Two patients could be booked with the same practitioner at the same time.

3. **The appointment time is stored as text.**  
   The program does not check whether the entered date or time is actually valid.

## 3. Suggested Improvements

Some possible improvements are:

- Check that the practitioner name is not empty.
- Check that the appointment time is not empty.
- Check whether a practitioner is already booked at the selected time.
- Validate that the appointment date and time are in the correct format.
- Allow appointments to be updated or cancelled.

## 4. Questions to Test My Understanding

### Question 1

What is the purpose of the following line?

    appointments.append(appointment)

### Question 2

What will happen if the following code is run?

    book_appointment("", "Dr. John Doe", "10:00 AM")

## My Answers

**Question 1:**  
[Write my answer here]

**Question 2:**  
[Write my answer here]


# Part E - Compare Human and AI Versions

| Question | Human Version | AI Version                                                                                               |
|---|---|----------------------------------------------------------------------------------------------------------|
| **Easy to understand?** | Yes. The code given in the lab was simple and easy to follow. | Yes. The AI version was also simple, but used `input()` to ask the user for information.                 |
| **Runs successfully?** | Yes. The code ran successfully and displayed the appointments. | Yes. The AI code ran successfully and allowed me to enter appointment details in the terminal.           |
| **Uses only required features?** | Yes. It used basic Python features such as lists, dictionaries and functions. | Yes. It used basic Python features and `input()` to collect information from the user.                   |
| **Adds assumptions?** | The code assumes that the appointment information entered is correct. | Yes. The AI assumed that the information entered by the user was valid.                                  |
| **Handles errors?** | Partly. The enhanced code checks if the patient name is blank. | No. The original AI version accepted blank and invalid information.                                      |
| **Could I explain it?** | Yes. I understand how the provided code stores and displays appointments. | Some What. I understand how the AI version asks for information but storing it I don't fully understand. |

# Part F - Verify Behaviour

The AI-generated version was tested using normal and unusual inputs to check how the program behaves.

## Test 1 - Normal Appointment

### Input

```text
Patient name: Alice Smith
Practitioner name: Dr. John Doe
Appointment time: 2024-07-20 10:00 AM
```

### Result

The appointment was recorded successfully and all the information was displayed correctly.

**Test Result: Pass**

---

## Test 2 - Blank Patient Name

### Input

```text
Patient name:
Practitioner name: Dr. John Doe
Appointment time: 2024-07-20 10:00 AM
```

### Result

The program accepted the appointment even though the patient name was blank.

**Test Result: Fail**

### Limitation

The AI version does not check whether the patient name is empty.

---

## Test 3 - Two Appointments for the Same Practitioner and Time

### First Appointment

```text
Patient name: Alice Smith
Practitioner name: Dr. John Doe
Appointment time: 2024-07-20 10:00 AM
```

### Second Appointment

```text
Patient name: Bob Johnson
Practitioner name: Dr. John Doe
Appointment time: 2024-07-20 10:00 AM
```

### Result

The current AI version does not check whether a practitioner is already booked at the selected time. Therefore, there is no protection against double bookings.

**Test Result: Fail**

### Limitation

The program needs a way to check existing appointments before adding another appointment for the same practitioner and time.

---

## Test 4 - Blank Practitioner Name

### Input

```text
Patient name: Alice Smith
Practitioner name:
Appointment time: 2024-07-20 10:00 AM
```

### Result

The appointment was accepted even though the practitioner name was blank.

**Test Result: Fail**

### Limitation

The program does not validate the practitioner name.

---

## Test 5 - Blank Appointment Time

### Input

```text
Patient name: Alice Smith
Practitioner name: Dr. John Doe
Appointment time:
```

### Result

The appointment was accepted even though the appointment time was blank.

**Test Result: Fail**

### Limitation

The program does not check whether an appointment time has been entered.

---

## Test 6 - Strange Input

### Input

```text
Patient name: 12345
Practitioner name: 67890
Appointment time: hello
```

### Result

The program accepted all of the values and recorded the appointment.

**Test Result: Fail**

### Limitation

The program accepts unusual or invalid information because it does not validate the entered data.


