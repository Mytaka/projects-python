class Barri:
    name = None
    age = None
    weight = None
    isOwner = None
    owner = None


    def __init__(self, name = None, age = None, weight = None, isOwner = None, owner = None):
        self.name = name
        self.age = age
        self.weight = weight
        self.isOwner = isOwner
        self.owner = owner 

        self.get_data()

    def get_data(self):
        print(self.name, 'age:', self.age, 'owner: ', self.owner)

barri1 = Barri('Kirik', 19, 80, True, 'Mytka')
barri2 = Barri('Barista', 19.5, 80.5, False, 'freedom')



