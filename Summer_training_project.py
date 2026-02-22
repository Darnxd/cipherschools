# Hospital Management System

# List to store patient records
patients = []

# Function to load patients from file
def load_patients():
    try:
        with open("patients.txt", "r") as file:
            for line in file:
                name, age, disease, patient_id = line.strip().split(",")
                patients.append({
                    "ID": patient_id,
                    "Name": name,
                    "Age": age,
                    "Disease": disease
                })
    except FileNotFoundError:
        pass

# Function to save patients to file
def save_patients():
    with open("patients.txt", "w") as file:
        for patient in patients:
            file.write(f"{patient['Name']},{patient['Age']},{patient['Disease']},{patient['ID']}\n")

# Function to add patient
def add_patient():
    name = input("Enter patient name: ")
    age = input("Enter age: ")
    disease = input("Enter disease: ")
    patient_id = input("Enter patient ID: ")

    patient = {
        "ID": patient_id,
        "Name": name,
        "Age": age,
        "Disease": disease
    }

    patients.append(patient)
    save_patients()
    print("Patient added successfully!")

# Function to view patients
def view_patients():
    if not patients:
        print("No patient records found.")
        return

    print("\nPatient Records:")
    for patient in patients:
        print(f"ID: {patient['ID']}")
        print(f"Name: {patient['Name']}")
        print(f"Age: {patient['Age']}")
        print(f"Disease: {patient['Disease']}")
        print("-" * 20)

# Function to search patient
def search_patient():
    search_id = input("Enter patient ID to search: ")

    for patient in patients:
        if patient["ID"] == search_id:
            print("Patient found:")
            print(patient)
            return

    print("Patient not found.")

# Function to delete patient
def delete_patient():
    delete_id = input("Enter patient ID to delete: ")

    for patient in patients:
        if patient["ID"] == delete_id:
            patients.remove(patient)
            save_patients()
            print("Patient deleted.")
            return

    print("Patient not found.")

# Main menu
def menu():
    load_patients()

    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Delete Patient")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            delete_patient()
        elif choice == "5":
            print("Exiting system...")
            break
        else:
            print("Invalid choice.")

# Run program
menu()
