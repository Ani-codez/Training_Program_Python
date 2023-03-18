doc={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
patient=input()[1:-1].split(',')

if patient.count("P")>patient.count("O"):
    if patient.count("P")>patient.count("E"):
        print(doc["P"])
    else:
        print(doc["E"])
else:
    if patient.count("O")>patient.count("E"):
        print(doc["O"])
    else:
        print(doc["E"])

