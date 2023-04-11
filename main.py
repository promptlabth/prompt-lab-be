from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from module.openapi import openapi_service


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://prompt.sutmeme.com"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hello_word() -> dict :
  return {"hello" : "world"}

app.include_router(openapi_service.router)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Read the PORT environment variable or default to 8000
    uvicorn.run(app, host="0.0.0.0", port=port)
