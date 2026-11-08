class Patient:
    def __init__(self, name, age, history):
        self.name = name
        self.age = age
        self.history = history
        
class Doctor:
    def __init__(self, name, specialization, appointments):
        self.name = name
        self.sp = specialization
        self.app = appointments
        
class Appointments:
    def __init__(self, patient, doctor, date, time):
        self.patient = patient
        self.d = doctor
        self.date = date
        self.time = time
        