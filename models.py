from typing import List, Optional
from pydantic import BaseModel, Field

class EmployeeModel(BaseModel):
    """Model representing a team in the company database.

    Attributes:
        name (str): The name of the employees.
        gender (str): gender of the employee.
        city (str): city where the employee is located
        country (str): country where the employee is from
        team (str): team the  employee belongs to
        todos (Optional [str]): todos of the employee 
    """
    name: str = Field(...)
    gender: str = Field (...)
    city: str = Field (...)
    country: str = Field (...)
    team: str = Field (...)
    todos: str = Field (...)
    

