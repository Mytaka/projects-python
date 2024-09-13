class Barri:
    name = None
    age = None
    weight = None
    isOwner = None
    owner = None

    def set_data(self, name, age, weight, isOwner, owner): #self - говорит что мы берем елементы из класе
        self.name = name
        self.age = age
        self.weight = weight
        self.isOwner = isOwner
        self.owner = owner 
    def get_data(self):
        print(self.name, 'age:', self.age, 'owner: ', self.owner)

barri1 = Barri()
barri1.set_data('Kirik', 19, 80, True, 'Mytka')
# barri1.name = 'Kirik'
# barri1.age = 19
# barri1.weight = 80
# barri1.isOwner = True
# barri1.owner = 'Mytka'

barri2 = Barri()
barri2.set_data('Barista', 19.5, 80.5, False, 'freedom')
# barri2.name = 'Barista'
# barri2.age = 19.5
# barri2.weight = 80.5
# barri2.isOwner = False

print(barri1.owner)
barri1.get_data()

