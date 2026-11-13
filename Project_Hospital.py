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