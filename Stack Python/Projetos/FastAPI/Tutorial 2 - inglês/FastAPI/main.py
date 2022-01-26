import json

from fastapi import FastAPI, Path, Query, Body, Depends, HTTPException
from models import Employee, User
from mongoengine import connect
from mongoengine.queryset.visitor import Q
from pydantic import BaseModel
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm #pega o token
from datetime import timedelta, datetime
from jose import jwt

app = FastAPI()
connect(db="hrms", host="localhost", port=27017)

#@app.get('/')
#def home():
#    return {"message": "Hello World"}

@app.get('/get_all_employees')
def get_all_employees():
    employees = json.loads(Employee.objects().to_json())

    #print(type(employees))
    #employees_list = json.loads(employees)
    #print(type(employees_list))

    return {"employees": employees}

@app.get('/get_employee/{emp_id}')
def get_employee(emp_id: int = Path(..., gt=0)): #valor digitado deve ser maior do que 0 (grater than)
    #print(emp_id)
    employee = Employee.objects.get(emp_id=emp_id) #segundo emp_id é o parâmetro

    employee_dict = {
        "emp_id": employee.emp_id,
        "name": employee.name,
        "age": employee.age,
        "teams": employee.teams
    }

    return employee_dict

@app.get('/search_employees')
def search_employees(name: str, age: int = Query(None, gt=18)):
    employees = json.loads(Employee.objects.filter(Q(name__icontains=name) | Q(age=age)).to_json())
    return {"employees": employees}

class NewEmployee(BaseModel):
    emp_id: int
    name: str
    age: int = Body(None, gt=18)
    teams: list

@app.post('/add_employee')
def add_employee(employee: NewEmployee):
    new_employee = Employee(emp_id=employee.emp_id, name=employee.name, age=employee.age, teams=employee.teams)
    new_employee.save()

    return {"message": "Employee was add!"}

class NewUser(BaseModel):
    username: str
    password: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

@app.post('/sign_up')
def sign_up(new_user: NewUser):
    user = User(username=new_user.username, password=get_password_hash(new_user.password))
    user.save()

    return {"Message": "New user created!"}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def authenticate_user(username, password):
    try:
        user = json.loads(User.objects.get(username=username).to_json())
        password_check = pwd_context.verify(password, user['password'])
        return password_check
    except User.DoesNotExist:
        return False
SECRET_KEY = "497764f7626a231d24938d38f5f66bad03ed5762684c499177f0a67e55d66ec6"
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta

    to_encode.update({"exp": expire})
    #print(to_encode)

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


@app.post('/token')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password

    if authenticate_user(username, password):
        access_token = create_access_token(data={"sub": username}, expires_delta=timedelta(minutes=30))
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Incorrect username or password...")
    #print(username, password)


@app.get('/')
def home(token: str = Depends(oauth2_scheme)):
    return {"token": token}



