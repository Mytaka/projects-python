class Building:
    year = None
    city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

        self.get_info()
        
    def get_info(self):
        print("Year: ", self.year, " City: ", self.city, sep="", end=" ")

class school(Building):
    pupils = 0
   
    def __init__(self, pupils, year, city):
        self.pupils = pupils
        super(school, self).__init__(year, city)

    def get_info(self):
        super().get_info()
        print("Pupils: ", self.pupils)



class home(Building):
    pass

class university(Building):
    pass

School = school(100, 108, "Krakov")
Home = home(20, "Poltava")
Unineversity = university(200, "Poltava")


