from fastapi import FastAPI
from module.openapi import openapi_service


app = FastAPI()

@app.get("/")
def hello_word() -> dict :
  return {"hello" : "world"}

app.include_router(openapi_service.router)
