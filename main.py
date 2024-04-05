from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from module.openapi import predict_service, tone_service
from module.usersapi import userapi_service
from module.facebook.controller import facebook_services

from module.promptapi import prompt_service


from controllers.v1.users_controller import userRouter
from controllers.v1.login_controller import loginRouter
from controllers.v1.facebook_controller import facebook_router

from controllers.v1.prompt_generate_controller import prompt_routers

from controllers.v1.tone_controller import tone_routers

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
    "https://1b8fg7zk-3000.asse.devtunnels.ms"
    "https://663b-1-46-153-144.ngrok-free.app",
    "https://babe-1-46-25-216.ngrok-free.app",
    "https://deploy-preview-38--comfy-cendol-1b50ad.netlify.app",
    "https://develop.promptlabai.com",
    "https://e18f-119-76-33-26.ngrok-free.app",
    "https://f537-171-97-97-42.ngrok-free.app"
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
app.include_router(facebook_services.router, prefix="/facebook")

app.include_router(loginRouter)


# app.include_router(testapit_service.router, prefix="/test")

app.include_router(tone_service.router)

app.include_router(userRouter)

app.include_router(prompt_routers)

app.include_router(tone_routers)

app.include_router(facebook_router)

if __name__ == "__main__":
    import uvicorn
    import os
    from dotenv import load_dotenv, find_dotenv

    # load_dotenv(find_dotenv())
    port = int(os.environ.get("PORT", 8080))  # Read the PORT environment variable or default to 8080
    uvicorn.run(app, host="0.0.0.0", port=port)
