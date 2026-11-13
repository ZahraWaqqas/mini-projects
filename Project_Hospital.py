class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.history = [] # List of strings for medical notes
        
class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.appointments = []
        
class Appointments:
    def __init__(self, patient, doctor, date, time):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

def add_patient(patient_list):
    name = input("Enter name: ")
    age = int(input("Enter age: "))

    new_patient = Patient(name, age)
    patient_list.append(new_patient)

    print(f"Patient {name} added.")


def add_doctor(doctor_list):
    name = input("Enter name: ")
    specialization = input("Enter specialization: ")

    new_doctor = Doctor(name, specialization)
    doctor_list.append(new_doctor)

    print(f"Doctor {name} ({specialization}) added.")


def find_patient(patient_list, name):
    """Helper to find a Patient object by name."""
    for p in patient_list:
        if p.name.lower() == name.lower():
            return p
    return None


def find_doctor(doctor_list, name):
    """Helper to find a Doctor object by name."""
    for d in doctor_list:
        if d.name.lower() == name.lower():
            return d
    return None


def book_appointment(patient_list, doctor_list):
    """Books an appointment if the doctor's time slot is free."""
    p_name = input("Enter patient name: ")
    d_name = input("Enter doctor name: ")
    date = input("Enter date (DD/MM): ")
    time = input("Enter time (HH:MM): ")

    # 1. Validate that the patient and doctor actually exist in the system
    patient = find_patient(patient_list, p_name)
    doctor = find_doctor(doctor_list, d_name)

    if not patient:
        print(f"Error: Patient '{p_name}' not found in records.")
        return
    if not doctor:
        print(f"Error: Doctor '{d_name}' not found in records.")
        return

    # 2. Conflict Detection Logic
    for existing_app in doctor.appointments:
        if existing_app.date == date and existing_app.time == time:
            print(f"ERROR: Time slot already booked for Dr. {doctor.name}.")
            return

    # 3. If no conflict, create and store the appointment
    new_appointment = Appointment(patient, doctor, date, time)
    doctor.appointments.append(new_appointment)

    print(f"Appointment booked for {patient.name} with Dr. {doctor.name} on {date} at {time}.")