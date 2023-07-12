
## run in local machine

step to run backend to local
1. create environment use command `python -m venv env`

2. activate a environment 



- windows `./env/Scripts/activate`
"NOTE" IF YOU RUN ON PYTHON version 3.11 upper you should run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted` on Powershell And run `./env/bin/Activate.ps1`

- Mac `source ./env/bin/activate`

3. install library from requirements.txt use command `pip install -r requirements.txt`

4. create a file `.env` in ./ folder and add OPENAI_KEY

5. use command `uvicorn main:app --reload` to run fastapi in your local

## run docker

docker run -d --name test-api-con -p 8000:8000 -e OPANAI_KEY test-api

