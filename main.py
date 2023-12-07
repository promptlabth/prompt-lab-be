from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from module.openapi import predict_service, tone_service
from module.usersapi import userapi_service

from module.promptapi import prompt_service

from firebase import init_firebase



app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://prompt.sutmeme.com",
    "https://promptlab.sutmeme.com",
    "https://tao-isaman-literate-fiesta-6r7477vgqxv35qx-3000.preview.app.github.dev",
    "https://promptlab-fe-git-dev-login-promptlab.vercel.app",
    "https://deploy-preview-10--comfy-cendol-1b50ad.netlify.app",
    "https://8b60-49-228-51-134.ngrok-free.app"
    "https://8b60-49-228-51-134.ngrok-free.app"
    "https://ac9b-1-47-138-60.ngrok-free.app",
    "https://deploy-preview-11--comfy-cendol-1b50ad.netlify.app",
    "https://promptlabai.com",
    "https://deploy-preview-14--comfy-cendol-1b50ad.netlify.app",
    "https://deploy-preview-15--comfy-cendol-1b50ad.netlify.app",
    "https://deploy-preview-33--comfy-cendol-1b50ad.netlify.app",
    "https://eaef-1-47-147-202.ngrok-free.app",
    "https://1b8fg7zk-3000.asse.devtunnels.ms"
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

app.include_router(predict_service.router)
app.include_router(userapi_service.router, prefix="/users")
app.include_router(prompt_service.router)


# app.include_router(testapit_service.router, prefix="/test")

app.include_router(tone_service.router)


if __name__ == "__main__":
    import uvicorn
    import os
    from dotenv import load_dotenv

    load_dotenv()
    port = int(os.environ.get("PORT", 8080))  # Read the PORT environment variable or default to 8080
    uvicorn.run(app, host="0.0.0.0", port=port)
