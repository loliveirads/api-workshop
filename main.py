from fastapi import FastAPI

app = FastAPI()

@app.get("/") # Request
def ola_mundo(): #Response
    return {"ola":"Mundo"}