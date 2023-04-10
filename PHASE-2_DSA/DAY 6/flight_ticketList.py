ticket_list=["AI567:MUM:LON:014",
             "AI077:MUM:LON:056",
             "BA896:MUM:LON:067",
             "SI267:MUM:SIN:145",
             "AI077:MUM:CAN:060",
             "SI267:BLR:MUM:148",
             "AI567:CHE:SIN:015",
             "AI077:MUM:SIN:050",
             "AI077:MUM:LON:051",
             "SI267:MUM:SIN:146"]

def find_passengers_flight(flight):
    for i in ticket_list:
        if i[:2]==flight:
            print(i)

def find_passengers_destination(dest):
    for i in ticket_list:
        if i.split(":")[2]==dest:
            print(i)

def find_passengers_per_flight():
    d={}
    for i in ticket_list:
        x=i.split(":")[0]
        if x not in d:
            d[x]=1
        else:
            d[x]+=1
    for i in d:
        print(i,":",d[i],"passengers")

def sort_passenger_list():
    return sorted(ticket_list)

print("Passengers with flight AI")
find_passengers_flight("AI")
print("Passengers with destination LON:")
find_passengers_destination("LON")
print("Passengers per Flight:")
find_passengers_per_flight()
print("Sorted List:")
print(sort_passenger_list())
