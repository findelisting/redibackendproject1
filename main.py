
from fastapi import FastAPI
from models import *
from dbt import RediBackEndProject
import uvicorn
from fastapi import HTTPException


app = FastAPI ()
db = RediBackEndProject ()



#employee###########################################################
@app.get ("/employees")
def getAllEmployees ():
    employees = db.getAllEmployees ()

    results = []

    for employee in employees:
        del employee["_id"]
        results.append(employee)

    return {"data": results}

  

#get one employee
@app.get ("/employees/{employee_name}")
def getOneEmployeeByName (employee_name: str):
   results = db.getOneEmployeeByName (name= employee_name)
   return {"data": results}

   
#create employee

#@app.post("/Employees")
#def insertEmployee(employee: EmployeeModel) -> dict[str, str]:
    # Validate the incoming data using the Pydantic model
 #   try:
        # Pass the EmployeeModel instance directly, not its dictionary representation
  #      db.insertEmployee(employee=employee)
   # except ValueError as e:
    #    raise HTTPException(status_code=422, detail=str(e))
    #
    #return {"message": "successful"}

@app.post ("/Employees/employeelist")
def insertEmployee (employee: EmployeeModel) -> dict [str, str]: 
    db.insertEmployee (employee = employee)
    return {"message": "successful"}

#delete employee
@app.delete ("/employees/{employee_name}")
def deleteEmployeeByName (employee_name: str):
    db.deleteEmployeeByName (name = employee_name)
    return {"message": "successful"}

#update the employee todo list by changing the entire list
@app.put("/employees/{employee_name}")
def updateEmployeeTodoByName(employee_name: str, todos: str):
    results = db.updateEmployeeTodoByName(employee_name, todos)
    if results.modified_count == 1:
        return {"message": "Employee todos updated successfully"}



#delete all employees
@app.delete("/employees")
def delete_all_employees():
    db.deleteAllEmployees()
    return {"message": "All employees deleted successfully"}





if __name__ == "__main__":
    uvicorn.run("main:app",
                host='',
                port=4557,
                reload=True,
                log_level="info")
