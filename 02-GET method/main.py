from fastapi import FastAPI
from typing import Optional

app = FastAPI()


# Sample data
users = [
    {"id": 1, "name": "Prathamesh", "age": 22},
    {"id": 2, "name": "Rahul", "age": 23},
    {"id": 3, "name": "Amit", "age": 21}
]


# 1. Basic GET method
@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI"
    }


# 2. GET all users
@app.get("/users")
def get_users():
    return {
        "users": users
    }


# 3. GET user using Path Parameter
@app.get("/users/{user_id}")
def get_user(user_id: int):

    for user in users:
        if user["id"] == user_id:
            return user

    return {
        "message": "User not found"
    }


# 4. GET user using Query Parameter
@app.get("/search")
def search_user(name: str):
    
    for user in users:
        if user["name"].lower() == name.lower():
            return user

    return {
        "message": "User not found"
    }


# 5. GET with Optional Query Parameter
@app.get("/filter")
def filter_users(age: Optional[int] = None):

    if age is None:
        return {
            "users": users
        }

    filtered_users = []

    for user in users:
        if user["age"] == age:
            filtered_users.append(user)

    return {
        "users": filtered_users
    }