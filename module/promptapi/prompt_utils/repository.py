from datetime import datetime

from sqlalchemy import and_, func
from model import database
from model.promptMessages import prompt_messages_model
from model.tones import tone_model
from model.languages import languages_model
from model.features import features_model
from model.users import users_model
from model.models import models_model
from sqlmodel import select


def getToneById (id) :
    with database.session_engine() as session:
        try:
            statement_tone = select(tone_model.Tones).where(tone_model.Tones.id == id)
            tone = session.exec(statement=statement_tone).one()
            return tone
        except:
            return False

def getLanguageById (id):
    with database.session_engine() as session:
        try:
            statement = select(languages_model.Languages).where(languages_model.Languages.id == id)
            language = session.exec(statement=statement).one()
            return language
        except:
            return False

def getFeaturById(id):
    with database.session_engine() as session:
        try:
            statement = select(features_model.Features).where(features_model.Features.id == id)
            feature = session.exec(statement=statement).one()
            return feature
        except:
            return False
        
def getUserByFirebaseId(firebase_id):
    with database.session_engine() as session:
        try:
            statement = select(users_model.Users).where(users_model.Users.firebase_id == firebase_id)
            user = session.exec(statement=statement).one()
            return user
        except:
            return False
        
def getModelAIById(model:str):
    with database.session_engine() as session:
        try:
            statement = select(models_model.Models).where(models_model.Models.model_name == model)
            modelResult = session.exec(statement=statement).one()
            return modelResult
        except:
            return False


def getMessagesToDay(user):
    with database.session_engine() as session:
        try:
            # Current date in YYYY-MM-DD format
            current_date = datetime.utcnow().date()

            # Modify the query to count messages for the current day
            statement_prompt = select([func.count()]).where(
                and_(
                    prompt_messages_model.Promptmessages.user_id == user.id,
                    func.date(prompt_messages_model.Promptmessages.date_time) == current_date
                )
            )

            # Execute the query and get the count
            total_messages_today = session.execute(statement_prompt).scalar()

            return total_messages_today
        except Exception as e:
            print(f"An error occurred: {e}")  # It's a good practice to log the exception
            return False