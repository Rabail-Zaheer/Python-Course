medical_cause = input("Did you have a medical cause? (Y/N): ").strip().upper()
if medical_cause == 'Y':   # Condition 1
    print("You are allowed")
else:
    atten = int(input("Enter the attendance of the student: "))

    if atten >= 75:   # Condition 2
        print("Allowed")
    else:
        print("Not allowed")
