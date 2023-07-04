from sqlmodel import Field, Session, SQLModel, create_engine, select
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

# global l_1, l_2

def create_data_in_db():
    with Session(engine) as session:

        t1 = tone_model.Tones(tone_name="สนุกสนาน")
        t2 = tone_model.Tones( tone_name="มั่นใจ")
        t3 = tone_model.Tones( tone_name="มืออาชีพ")
        t4 = tone_model.Tones( tone_name="หรูหรา")
        t5 = tone_model.Tones( tone_name="มีการศึกษา")
        t6 = tone_model.Tones( tone_name="มีความสุข")
        t7 = tone_model.Tones( tone_name="ทันสมัย")
        t8 = tone_model.Tones( tone_name="ย้อนยุค")
        t9 = tone_model.Tones( tone_name="Funny")
        t10 = tone_model.Tones( tone_name="Confident")
        t11 = tone_model.Tones( tone_name="Professional")
        t12 = tone_model.Tones( tone_name="Luxury")
        t13 = tone_model.Tones( tone_name="Educational")
        t14 = tone_model.Tones( tone_name="Happy")
        t15 = tone_model.Tones( tone_name="Modern")
        t16 = tone_model.Tones( tone_name="Retro")
        l_1 = languages_model.Languages(language_name="Th", tones=[t1, t2, t3, t4, t5, t6, t7, t8, t9])
        l_2 = languages_model.Languages(language_name="Eng", tones=[ t10, t11, t12, t13, t14, t15, t16])
        session.add(l_1)
        session.add(l_2)
        session.commit()
        session.refresh(l_1)
        session.refresh(l_2)

        f1 = features_model.Features( name="เขียนแคปชั่นขายของ",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createSellingPost")
        f2 = features_model.Features( name="ช่วยคิดคอนเทนต์",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createIdeaContent")
        f3 = features_model.Features( name="เขียนบทความ",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createArticle")
        f4 = features_model.Features( name="เขียนสคริปวิดีโอสั้น",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createShortVideoScripts")
        f5 = features_model.Features( name="เขียนประโยคเปิดคลิป",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createClickBaitWord")
        f6 = features_model.Features( name="Create Selling Post",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createSellingPost")
        f7 = features_model.Features( name="Create idea contents",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createIdeaContent")
        f8 = features_model.Features( name="Create Artical",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createArticle")
        f9 = features_model.Features( name="Create Video Scripts",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createShortVideoScripts")
        f10 = features_model.Features( name="Create Click Bait Word",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createClickBaitWord")

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
        session.refresh(f1)
        session.refresh(f2)
        session.refresh(f3)
        session.refresh(f4)
        session.refresh(f5)
        session.refresh(f6)
        session.refresh(f7)
        session.refresh(f8)
        session.refresh(f9)
        session.refresh(f10)

        

# create_data_in_db()


# !!! below THIS CODE IS EXAMPLE FOR CREATE DATABASE IN RELATION QUERY
# def test_database():
#     with Session(engine) as session:
#         statement = select(languages_model.Languages).where(languages_model.Languages.id == 25)
#         result = session.exec(statement=statement)
#         l_1 = result.one()

#         a1 = tone_model.Tones(
#             tone_name="เทส",
#             language=l_1
#         )

#         session.add(a1)
#         session.commit()
#         session.refresh(a1)

# test_database()
# !!! upper THIS CODE IS EXAMPLE FOR CREATE DATABASE IN RELATION QUERY


# code for create tone



# code for create feature
def create_feature():
    
    f1 = features_model.Features( name="เขียนแคปชั่นขายของ",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createSellingPost")
    f2 = features_model.Features( name="ช่วยคิดคอนเทนต์",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createIdeaContent")
    f3 = features_model.Features( name="เขียนบทความ",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createArticle")
    f4 = features_model.Features( name="เขียนสคริปวิดีโอสั้น",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createShortVideoScripts")
    f5 = features_model.Features( name="เขียนประโยคเปิดคลิป",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createClickBaitWord")
    f6 = features_model.Features( name="Create Selling Post",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createSellingPost")
    f7 = features_model.Features( name="Create idea contents",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createIdeaContent")
    f8 = features_model.Features( name="Create Artical",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createArticle")
    f9 = features_model.Features( name="Create Video Scripts",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createShortVideoScripts")
    f10 = features_model.Features( name="Create Click Bait Word",date_of_create=datetime.now(),url="https://promptlab.sutmeme.com/createClickBaitWord")

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

# create tone
def create_tone():
    l_1 = languages_model.Languages(language_name="Th")
    l_2 = languages_model.Languages(language_name="Eng")
    

    session = Session(engine)

    session.add(l_1)
    session.add(l_2)

    session.commit()
    session.refresh(l_1)
    session.refresh(l_2)

    t1 = tone_model.Tones(tone_name="สนุกสนาน", language=l_1)
    t2 = tone_model.Tones( tone_name="มั่นใจ", language=l_1)
    t3 = tone_model.Tones( tone_name="มืออาชีพ", language=l_1)
    t4 = tone_model.Tones( tone_name="หรูหรา", language=l_1)
    t5 = tone_model.Tones( tone_name="มีการศึกษา", language=l_1)
    t6 = tone_model.Tones( tone_name="มีความสุข", language=l_1)
    t7 = tone_model.Tones( tone_name="ทันสมัย", language=l_1)
    t8 = tone_model.Tones( tone_name="ย้อนยุค", language=l_1)
    t9 = tone_model.Tones( tone_name="Funny", language=l_2)
    t10 = tone_model.Tones( tone_name="Confident", language=l_2)
    t11 = tone_model.Tones( tone_name="Professional", language=l_2)
    t12 = tone_model.Tones( tone_name="Luxury", language=l_2)
    t13 = tone_model.Tones( tone_name="Educational", language=l_2)
    t14 = tone_model.Tones( tone_name="Happy", language=l_2)
    t15 = tone_model.Tones( tone_name="Modern", language=l_2)
    t16 = tone_model.Tones( tone_name="Retro", language=l_2)
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


# create_Language()
# create_feature()
# create_tone()

    