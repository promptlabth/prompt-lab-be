from datetime import datetime

from sqlalchemy import and_, func
from model import database
from model.plans.plans_model import Plans
from model.promptMessages import prompt_messages_model
from model.subscriptions_payments import subscriptions_payments_model
from model.tones import tone_model
from model.languages import languages_model
from model.features import features_model
from model.users import users_model
from model.models import models_model
from model.coins import coins_model
from sqlmodel import select, col


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


def getMessagesThisMonth(user):
    with database.session_engine() as session:
        try:
            # Get the current year and month
            current_year = datetime.utcnow().year
            current_month = datetime.utcnow().month

            # Modify the query to count messages for the current month
            statement_prompt = select([func.count()]).where(
                and_(
                    prompt_messages_model.Promptmessages.user_id == user.id,
                    func.extract('year', prompt_messages_model.Promptmessages.date_time) == current_year,
                    func.extract('month', prompt_messages_model.Promptmessages.date_time) == current_month
                )
            )

            # Execute the query and get the count
            total_messages_this_month = session.execute(statement_prompt).scalar()

            return total_messages_this_month
        except Exception as e:
            print(f"An error occurred: {e}")  # It's a good practice to log the exception
            return False

def getMaxMessageByUserId(user):
    with database.session_engine() as session:
        try:
            # Query to check for active subscription and get maxMessages
            query = select(Plans.maxMessages).join(
                subscriptions_payments_model.Subscriptions_Payments, subscriptions_payments_model.Subscriptions_Payments.plan_id == Plans.id
            ).where(
                subscriptions_payments_model.Subscriptions_Payments.user_id == user.id,
                subscriptions_payments_model.Subscriptions_Payments.subscription_status == 'active'
            ).order_by(col(subscriptions_payments_model.Subscriptions_Payments.id).desc())

            # Execute the query and fetch the result
            result = session.execute(query).first()

            # If an active subscription is found, return its maxMessages
            if result:
                return result[0]

            # If no active subscription, query for the free plan's maxMessages
            free_plan_query = select(Plans.maxMessages).where(Plans.planType == 'Free')
            free_plan_result = session.execute(free_plan_query).first()

            return free_plan_result[0] if free_plan_result else None

        except Exception as e:
            print(f"An error occurred: {e}")  # It's a good practice to log the exception
            return False
        
def getCoinBalanceByUserId(id):
    with database.session_engine() as session:
        try:
            statement = select(coins_model.Coins).where(users_model.Users.id == id)
            coin = session.exec(statement=statement).one()
            return coin
        except:
            return False

def getPlanByUserId(id):
    with database.session_engine() as session:
        # get plan id from subscription payment
        try:
            statement = select(subscriptions_payments_model.Subscriptions_Payments).where(subscriptions_payments_model.Subscriptions_Payments.user_id == id)
            subscription = session.execute(statement).first()

            # # if subscription is not found
            if (subscription is None):
                # query free plan
                statement = select(Plans).where(Plans.planType == "Free")
                plan = session.execute(statement).first()
                return plan[0]
            
            # if subscription is found return plan
            else:
                planId = subscription[0].plan_id
                statement = select(Plans).where(Plans.id == planId)
                plan = session.execute(statement).first()
                return plan[0]

        except:
            return False
