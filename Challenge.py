class Me(object):
    def __init__(self, height, weight, hair_color, eye_color):
        self.height = height 
        self.weight = weight
        self.hair_color = hair_color
        self.eye_color = eye_color
    
    def tellHeight(self):
        print("Juan is very tall. He is 11 feet tall")

    def tellWeight(self):
        print("Juan is 1000 pounds")

    def tellHairColor(self):
        print("Juan has brown hair")

    def tellEyeColor(self):
        print("Juan's eyes are brown")

juan = Me(11, 1000, "brown", "brown")
print(juan.tellHeight())
print(juan.tellWeight())
print(juan.tellHairColor())
print(juan.tellEyeColor())

print(juan.height)

print(juan.weight)

print(juan.hair_color)

print(juan.eye_color)
