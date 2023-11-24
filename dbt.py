from pymongo import MongoClient
from models import EmployeeModel

from pymongo import MongoClient

class RediBackEndProject:
    # Connect to MongoDB on localhost
    client = MongoClient("localhost", 27017)

    # Access the "redibackendproject" database
    db = client.redibackendproject

    # Define example documents for each collection
    exampleEmployee = {
        "name": "John Doe",
        "gender": "Male",
        "city": "Example City",
        "country": "Example Country",
        "team": "Example Team",
        "todos": "Go Fishing"
    }
    employeesCollection = db.employeesCollection

    # Insert the example employee document into the "employeesCollection" collection
    employeesCollection.insert_one(exampleEmployee)


    # read all employees
    def getOneEmployeeByName(self, name: str):
        return self.employeesCollection.find_one({"name": name}, {"name": 1,
            "gender": 1,
            "city": 1,
            "country": 1,
            "team": 1, "todos": 1, "_id": False})

    # read all employees
    def getAllEmployees(self):
        return self.employeesCollection.find({})

    # insert
    def insertEmployee(self, employee: EmployeeModel) -> exampleEmployee:
        return self.employeesCollection.insert_one({
            "name": employee.name,
            "gender": employee.gender,
            "city": employee.city,
            "country": employee.country,
            "team": employee.team,
            "todos": employee.todos
            })


    

    #update employee todo list by changing the entire todo list
    
    def updateEmployeeTodoByName(self, name: str, todos: str):
        update_query = {"$set": {"todos": todos}}
        return self.employeesCollection.update_one({"name": name}, update_query)


    # delete one employee by name
    def deleteEmployeeByName(self, name: str):
        return self.employeesCollection.delete_one({"name": name})

    # delete all employees from the dataset
    def deleteAllEmployees(self):
        return self.employeesCollection.delete_many({})
    