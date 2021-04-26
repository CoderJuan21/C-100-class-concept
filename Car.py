class Car(object):
    def __init__(self, color, model, company, speed_limit):
        self.color = color 
        self.model = model
        self.company = company
        self.speed_limit = speed_limit
    
    def start(self):
        print("the car has started")

    def stopYourself(self):
        print("the car stopped")

    def accelerate(self):
        print("the car is accelerating")

    def change_gear(self):
        print("gear changed")


tesla = Car("blue", "A2", "Tesla", 140)
print(tesla.start())
print(tesla.stopYourself())
print(tesla.accelerate())
print(tesla.change_gear())
