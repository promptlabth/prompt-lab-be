from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from module.openapi import openapi_service, predict_service, tone_service
from module.usersapi import userapi_service
from module.testapi import testapit_service


from firebase import init_firebase

# this code for create table in database is will be execute whne you run a api server....
import model
from model.database import create_database
create_database()


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://prompt.sutmeme.com",
    "https://promptlab.sutmeme.com",
    "https://tao-isaman-studious-engine-pgqpqq7rvvq2r5rw-3000.preview.app.github.dev",
    "https://promptlab-fe-git-dev-login-promptlab.vercel.app",
    "https://deploy-preview-9--comfy-cendol-1b50ad.netlify.app"
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
app.include_router(openapi_service.router_with_dependency)
app.include_router(predict_service.router)


app.include_router(userapi_service.router, prefix="/users")


# app.include_router(testapit_service.router, prefix="/test")

app.include_router(tone_service.router)


if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8080))  # Read the PORT environment variable or default to 8080
    uvicorn.run(app, host="0.0.0.0", port=port)
