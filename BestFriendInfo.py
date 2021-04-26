class BestFriendInfo(object):
    def __init__(self, height, weight, hair_color, eye_color):
        self.height = height 
        self.weight = weight
        self.hair_color = hair_color
        self.eye_color = eye_color
    
    def tellHeight(self):
        print("My friend is very short. He is 2 feet tall")

    def tellWeight(self):
        print("My friend is 140 pounds")

    def tellHairColor(self):
        print("My friend has black hair")

    def tellEyeColor(self):
        print("My friend's eyes are blue")

friend = BestFriendInfo(2, 140, "black", "blue")
print(friend.tellHeight())
print(friend.tellWeight())
print(friend.tellHairColor())
print(friend.tellEyeColor())

print(friend.height)

print(friend.weight)

print(friend.hair_color)

print(friend.eye_color)
