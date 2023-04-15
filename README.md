
## run in local machine

uvicorn main:app --reload

## run docker

docker run -d --name test-api-con -p 8000:8000 -e OPANAI_KEY test-api

