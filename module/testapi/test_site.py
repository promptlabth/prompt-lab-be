from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine
import pytest 
from module.testapi import testapit_service

from model import database


app = FastAPI()
app.include_router(testapit_service.router)
URL = "sqlite:///database.db"
engine = create_engine(URL)
client = TestClient(app)


# client = TestClient(app=)

@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    SQLModel.metadata.create_all(engine)


def test_app():
    result = client.get("/testPath")
    print(result)
    assert result.json()['test'] == 'test'