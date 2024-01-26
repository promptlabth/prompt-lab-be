import openai
import os 
import json
import vertexai
from vertexai.preview.language_models import TextGenerationModel as Preview_TextGenerationModel
from vertexai.language_models import TextGenerationModel
from google.oauth2 import service_account
import os

openai.api_key = os.environ.get("OPENAI_KEY")

prompt_format ={
    "th": """ Improve a social media announcement from this [{input}]
            to have more information that relavent about this topic and then add some words, hashtags, and emojis to it. give more expression, information
            **all information must be real** **you must keep same feeling of text**[เป็นภาษาไทยเท่านั้น]""",
            
    "eng":""" Improve a social media announcement from this [{input}]
            to have more information that relavent about this topic and then add some words, hashtags, and emojis to it. give more expression, information
            **all information must be real** **you must keep same feeling of text**"""
}

def openAiImproveCaption(input_message, language):
    print(language)
    prompt = prompt_format[language]
    prompt = prompt.format(
        input = input_message
    ) 
    
    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ]
    )
    assistant_reply = result['choices'][0]['message']['content']

    return assistant_reply

def vertexAiImproveCaption(input_message, language):
    model = {
        "model": "text-bison-32k",
        "parametor":
            {
                "max_output_tokens": 5000,
                "temperature": 0.3,
                "top_p": 0.8,
                "top_k": 40
            }
    }
    credential = service_account.Credentials.from_service_account_file("gcp_sa_key.json")
    vertexai.init(project=os.environ.get("GCP_PROJECT_ID"), location="us-central1", credentials=credential)
    
    vertex_model = Preview_TextGenerationModel.from_pretrained(model["model"]) 
    parametor = model["parametor"]
    prompt = prompt_format[language]
    prompt = prompt.format(
        input = input_message,
    )
    resp = vertex_model.predict(prompt, **parametor)

    return resp.text
    
