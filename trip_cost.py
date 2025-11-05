def hotelcost(nights):
    return nights * 140

def plane_ride_cost(city):
    if city == "Mumbai":
        return 183
    elif city == "New Delhi":
        return 220
    elif city == "Pune":
        return 222
    elif city == "Satana":
        return 475
    
def rentalcar_cost(days):
    if days >= 7:
        return days * 40 - 50
    elif days >= 3:
        return days * 40 - 20
    else:
        return days * 40
    
def trip_cost(city, days):
    return plane_ride_cost(city) + rentalcar_cost(days)

print("Car rental:", rentalcar_cost(10))
print("plane ride:", plane_ride_cost(4))
print("hotel cost:", hotelcost(7))
print("trip cost:", trip_cost( "Mumbai", 4))