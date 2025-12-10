class vehecile:
    def __init__(self, name, maxi, mil):
        self.name = name
        self.maxi = maxi
        self.mil = mil
class bus(vehecile):
    pass

school_bus = bus("School Ehicher", 200, 30)
print(f"name:", school_bus.name, "maxi:", school_bus.maxi, "mil:", school_bus.mil)