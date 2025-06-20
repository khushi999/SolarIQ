from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/greet")
def greet():
    return {"message": "Hello from the SolarIQ API!"} 