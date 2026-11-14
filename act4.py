class Mobile:
    charging_type = "type-c"
    
    def __init__(self, model, os):
        self.model = model
        self.os = os
        
    def brandName(self):
        return "{} runs on {}". format(self.model, self.os)

smartphone1= Mobile("Samsung", "android")
smartphone2= Mobile("iPhone", "ios")

print(smartphone1.brandName())
print(smartphone2.brandName())