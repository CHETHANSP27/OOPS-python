#example
class employee:
    #special method/magic method/dunder method - constructor
    def __init__(self):
        self.id = 123
        self.salary = 50000 
        self.designation = "SDE"
        print("attributes are initiated-called itself when object is created")

    def travel(self, destination):
        print("methods are called manually")
        print(f"Employee is now travelling to {destination}")

#creating an object or instance
sam=employee()
# print(sam.salary)
sam.travel("Mysuru")
print(type(sam))