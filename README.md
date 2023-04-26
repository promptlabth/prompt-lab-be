
## run in local machine

step to run backend to local
1. create environment use command `python -m venv {ENV NAME}`

2. activate a environment 
- windows `./{ENV NAME}/Scripts/activate`
- Mac ....

3. install library from requirements.txt use command `pip install -r requirements.txt`

4.create a file `.env` in ./ folder and add OPENAI_KEY

5. use command `uvicorn main:app --reload` to run fastapi in your local

uvicorn main:app --reload

## run docker

docker run -d --name test-api-con -p 8000:8000 -e OPANAI_KEY test-api

