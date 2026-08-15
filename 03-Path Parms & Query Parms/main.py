from fastapi import FastAPI
from typing import Optional

app = FastAPI()


# Sample data
users = [
    {"id": 1, "name": "Prathamesh", "age": 22, "city": "Pune"},
    {"id": 2, "name": "Rahul", "age": 23, "city": "Mumbai"},
    {"id": 3, "name": "Amit", "age": 21, "city": "Kolhapur"},
]

# 1. PATH PARAMETER

@app.get("/users/{user_id}")
def get_user(user_id: int):
    """
    Path parameter example.

    URL:
    /users/1
    /users/2
    /users/3
    """

    for user in users:
        if user["id"] == user_id:
            return user

    return {
        "message": "User not found"
    }


# 2. QUERY PARAMETER

@app.get("/search")
def search_user(name: str):
    """
    Query parameter example.

    URL:
    /search?name=Prathamesh
    """

    for user in users:
        if user["name"].lower() == name.lower():
            return user

    return {
        "message": "User not found"
    }


# 3. MULTIPLE QUERY PARAMETERS

@app.get("/users/search")
def search_users(
    city: str,
    age: Optional[int] = None
):
    """
    Multiple query parameters.

    Examples:

    /users/search?city=Pune

    /users/search?city=Pune&age=22
    """

    result = []

    for user in users:

        if user["city"].lower() == city.lower():

            if age is None or user["age"] == age:
                result.append(user)

    return {
        "users": result
    }

# 4. PATH PARAMETER + QUERY PARAMETER

@app.get("/users/{user_id}/details")
def user_details(
    user_id: int,
    include_city: bool = True
):
    """
    Path parameter + Query parameter.

    Example:

    /users/1/details

    /users/1/details?include_city=false
    """

    for user in users:

        if user["id"] == user_id:

            if include_city:
                return user

            return {
                "id": user["id"],
                "name": user["name"],
                "age": user["age"]
            }

    return {
        "message": "User not found"
    }


@app.get("/")
def home():
    return {
        "message": "FastAPI Path and Query Parameters"
    }