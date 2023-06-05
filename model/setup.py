from sqlmodel import Field, Session, SQLModel, create_engine
import os
from datetime import datetime
from model.languages import languages_model
from model.features import features_model
from model.tones import tone_model
now = datetime.now()
DATABASE_USER = os.environ.get("DB_USER")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
DATABASE_HOST = os.environ.get("DB_HOST")
DATABASE_PORT = os.environ.get("DB_PORT")
DATABASE_NAME = os.environ.get("DB_NAME")


postgres_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

engine = create_engine(postgres_URL, echo=True, future=True)
def create_Tone():
    l_1 = languages_model.Languages(id = 3,language_name="Th")
    l_2 = languages_model.Languages(id =4,language_name="Eng")
    

    session = Session(engine)

    session.add(l_1)
    session.add(l_2)

    session.commit()
    session.close()

def create_feature():
    
    f1 = features_model.Features(id=1, name="เขียนแคปชั่นขายของ",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createSellingPost")
    f2 = features_model.Features(id=2, name="ช่วยคิดคอนเทนต์",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createIdeaContent")
    f3 = features_model.Features(id=3, name="เขียนบทความ",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createArticle")
    f4 = features_model.Features(id=4, name="เขียนสคริปวิดีโอสั้น",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createShortVideoScripts")
    f5 = features_model.Features(id=5, name="เขียนประโยคเปิดคลิป",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createClickBaitWord")
    f6 = features_model.Features(id=6, name="Create Selling Post",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createSellingPost")
    f7 = features_model.Features(id=7, name="Create idea contents",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createIdeaContent")
    f8 = features_model.Features(id=8, name="Create Artical",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createArticle")
    f9 = features_model.Features(id=9, name="Create Video Scripts",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createShortVideoScripts")
    f10 = features_model.Features(id=10, name="Create Click Bait Word",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createClickBaitWord")

    session = Session(engine)

    session.add(f1)
    session.add(f2)
    session.add(f3)
    session.add(f4)
    session.add(f5)
    session.add(f6)
    session.add(f7)
    session.add(f8)
    session.add(f9)
    session.add(f10)


    session.commit()
    session.close()

def create_tone():
    t1 = tone_model.Tones(id=1,tone_name="สนุกสนาน",language_id=1)
    t2 = tone_model.Tones(id=2, tone_name="มั่นใจ", language_id=1)
    t3 = tone_model.Tones(id=3, tone_name="มืออาชีพ", language_id=1)
    t4 = tone_model.Tones(id=4, tone_name="หรูหรา", language_id=1)
    t5 = tone_model.Tones(id=5, tone_name="มีการศึกษา", language_id=1)
    t6 = tone_model.Tones(id=6, tone_name="มีความสุข", language_id=1)
    t7 = tone_model.Tones(id=7, tone_name="ทันสมัย", language_id=1)
    t8 = tone_model.Tones(id=8, tone_name="ย้อนยุค", language_id=1)
    t9 = tone_model.Tones(id=9, tone_name="Funny", language_id=2)
    t10 = tone_model.Tones(id=10, tone_name="Confident", language_id=2)
    t11 = tone_model.Tones(id=11, tone_name="Professional", language_id=2)
    t12 = tone_model.Tones(id=12, tone_name="Luxury", language_id=2)
    t13 = tone_model.Tones(id=13, tone_name="Educational", language_id=2)
    t14 = tone_model.Tones(id=14, tone_name="Happy", language_id=2)
    t15 = tone_model.Tones(id=15, tone_name="Modern", language_id=2)
    t16 = tone_model.Tones(id=16, tone_name="Retro", language_id=2)
    session = Session(engine)
    session.add(t1)
    session.add(t2)
    session.add(t3)
    session.add(t4)
    session.add(t5)
    session.add(t6)
    session.add(t7)
    session.add(t8)
    session.add(t9)
    session.add(t10)
    session.add(t11)
    session.add(t12)
    session.add(t13)
    session.add(t14)
    session.add(t15)
    session.add(t15)
    session.add(t16)
    
    session.commit()
    session.close()


    