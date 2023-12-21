from pydantic import BaseModel

class GenerateMessageRequest(BaseModel):
    """
    this calss is model for Requset to Generate a message
    """
    input_message: str
    tone_id: int
    feature_id: int

class GenerateMessageResponse(BaseModel):
    """
    this class is model for Response a generate message
    """
    reply: str
    error: str
