from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI"
    }


@app.get("/about")
def about():
    return {
        "application": "FastAPI Demo",
        "version": "1.0"
    }


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }


@app.get("/search")
def search(name: str):
    return {
        "search_name": name
    }