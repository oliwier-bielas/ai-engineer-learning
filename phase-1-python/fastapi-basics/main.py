from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {message: "Hello fastapi! I'm going to learn you fast :)"}
