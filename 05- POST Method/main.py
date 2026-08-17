from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# ==========================================
# Pydantic Model
# ==========================================

class User(BaseModel):
    name: str
    age: int
    email: str
    city: str

# Temporary database

users = []

# 1. Basic POST Method


@app.post("/users")
def create_user(user: User):

    users.append(user.model_dump())

    return {
        "message": "User created successfully",
        "user": user
    }

# 2. POST Method with ID


@app.post("/users/{user_id}")
def create_user_with_id(user_id: int, user: User):

    new_user = {
        "id": user_id,
        "name": user.name,
        "age": user.age,
        "email": user.email,
        "city": user.city
    }

    users.append(new_user)

    return {
        "message": "User created successfully",
        "user": new_user
    }


# GET - See created users

@app.get("/users")
def get_users():

    return {
        "users": users
    }