from model import database
from model.tones import tone_model
from model.languages import languages_model
from model.features import features_model
from sqlmodel import select


def get_tone_by_id (id) :
    with database.session_engine() as session:
        try:
            statement_tone = select(tone_model.Tones).where(tone_model.Tones.id == id)
            tone = session.exec(statement=statement_tone).one()
            return tone
        except:
            return False

def get_language_by_id (id):
    with database.session_engine() as session:
        try:
            statement = select(languages_model.Languages).where(languages_model.Languages.id == id)
            language = session.exec(statement=statement).one()
            return language
        except:
            return False

def get_feature_by_id(id):
    with database.session_engine() as session:
        try:
            statement = select(features_model.Features).where(features_model.Features.id == id)
            feature = session.exec(statement=statement).one()
            return feature
        except:
            return False