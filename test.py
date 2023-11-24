import unittest
from fastapi.testclient import TestClient

from main import app
from models import EmployeeModel


class TestEmployeeAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_all_employees(self):
        response = self.client.get("/employees")
        self.assertEqual(response.status_code, 200)
        

    def test_get_one_employee(self):
        employee_name = "John Doe"  
        response = self.client.get(f"/employees/{employee_name}")
        self.assertEqual(response.status_code, 200)
        


    def test_insert_employee(self):
         # Create an instance of EmployeeModel with valid data
        valid_employee_data = {
            "name": "Isaac Koomson",
            "gender": "Male",
            "city": "New York",
            "country": "Germany",
            "team": "HR",
            "todos": "finish the back end code"
        }

        # Send a POST request with the valid data
        response = self.client.post("/Employees/employeelist", json=valid_employee_data)

        # Assert that the request was successful (status code 200)
        self.assertEqual(response.status_code, 200)

    #def test_insert_employee(self):
     #   employee_data = {
      #      "name": "Isaac Koomson",
       #     "gender": "Male",
        #    "city": "New York",
         #   "country": "Germany",
          #  "team": "HR",
           # "todos": "finish the back end code"
        #}
        #response = self.client.post("/insertEmployee", json=employee_data)
        #self.assertEqual(response.status_code, 200)

    #def test_update_todo(self):
     #   employee_name = "Isaac Koomson"  
      #  todos = "go home"
       # response = self.client.put(f"/employees/{employee_name}", json={"todos": todos})
        #print (response.content)
        #self.assertEqual(response.status_code, 200)
    def test_update_todo(self):
        employee_name = "Isaac Koomson"  
        todos = "Gohome"
        response = self.client.put(f"/employees/{employee_name}", json={"todos": todos})

        # Print the response content for debugging purposes
        print(response.content)

        # Assert that the request was successful (status code 200)
        self.assertEqual(response.status_code, 200)    

    def test_delete_employee(self):
        employee_name = "Isaac Koomson"  
        response = self.client.delete(f"/employees/{employee_name}")
        self.assertEqual(response.status_code, 200)
        


if __name__ == "__main__":
    unittest.main()
