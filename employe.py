class Employee:
  def __init__(self, name, position):
    self.name = name
    self.position = position
    
  def get_details(self):
    return f"Employee Name: {self.name}, Position: {self.position}"
    
  def __del__(self):
    print(f"Deleting Employee: {self.name}")
    
  @staticmethod
  def create_object():
    print("Creating an Employee object")
    obj = Employee("John Doe", "Software Engineer")
    return obj
    
print("calling create_object")
object = Employee.create_object()
print(object.get_details())
print("End of script")