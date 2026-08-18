from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Pydantic Model

class User(BaseModel):
    name: str
    age: int
    email: str
    city: str


# Temporary Database

users = [
    {
        "id": 1,
        "name": "Prathamesh",
        "age": 22,
        "email": "prathamesh@gmail.com",
        "city": "Pune"
    },
    {
        "id": 2,
        "name": "Rahul",
        "age": 23,
        "email": "rahul@gmail.com",
        "city": "Mumbai"
    },
    {
        "id": 3,
        "name": "Amit",
        "age": 21,
        "email": "amit@gmail.com",
        "city": "Kolhapur"
    }
]


# GET - Get all users

@app.get("/users")
def get_users():
    return {
        "users": users
    }

# GET - Get single user

@app.get("/users/{user_id}")
def get_user(user_id: int):

    for user in users:
        if user["id"] == user_id:
            return user

    return {
        "message": "User not found"
    }


# PUT - Update user

@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):

    for user in users:

        if user["id"] == user_id:

            user["name"] = updated_user.name
            user["age"] = updated_user.age
            user["email"] = updated_user.email
            user["city"] = updated_user.city

            return {
                "message": "User updated successfully",
                "user": user
            }

    return {
        "message": "User not found"
    }


# DELETE - Delete user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    for user in users:

        if user["id"] == user_id:

            users.remove(user)

            return {
                "message": "User deleted successfully",
                "user": user
            }

    return {
        "message": "User not found"
    }