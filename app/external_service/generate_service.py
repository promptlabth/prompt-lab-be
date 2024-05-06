import openai
import os

import json
import vertexai
from vertexai.preview.language_models import TextGenerationModel as Preview_TextGenerationModel
from vertexai.generative_models import GenerativeModel 
import anthropic
from google.oauth2 import service_account
 

class GenerateService:

    def __init__(self) -> None:
        openai.api_key = os.environ.get("OPENAI_KEY")
        credential = service_account.Credentials.from_service_account_file("gcp_sa_key.json")
        vertexai.init(project=os.environ.get("GCP_PROJECT_ID"), location="asia-southeast1", credentials=credential)
        self.anthropic_client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY")
)

    def generateMessageOpenAI(self, input_prompt: str):
        result = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": input_prompt},
            ]
        )
        assistant_reply = result['choices'][0]['message']['content']
        return assistant_reply
    
    def getModelAndParameter(self, feature_name: str):
        model_list = {
        "เขียนแคปชั่นขายของ": {
            "model": "gemini-1.5-pro-preview-0409",
            "parametor":
                {
                    "max_output_tokens": 1024,
                    "temperature": 0.6,
                    "top_p": 0.8,
                    "top_k": 40
                }
        },
        "ช่วยคิดคอนเทนต์": {
            "model": "gemini-1.5-pro-preview-0409",
            "parametor":
                {
                    "max_output_tokens": 1024,
                    "temperature": 0.2,
                    "top_p": 0.8,
                    "top_k": 40
                }
        },
        "เขียนบทความ": {
            "model": "gemini-1.5-pro-preview-0409",
            "parametor":
                {
                    "max_output_tokens": 5500,
                    "temperature": 0.2,
                    "top_p": 0.8,
                    "top_k": 40
                }
        },
        "เขียนสคริปวิดีโอสั้น": {
            "model": "gemini-1.5-pro-preview-0409",
            "parametor":
                {
                    "max_output_tokens": 6000,
                    "temperature": 0.4,
                    "top_p": 0.8,
                    "top_k": 40
                }
        },
        "เขียนประโยคเปิดคลิป": {
            "model":"gemini-1.5-pro-preview-0409",
            "parametor":
                {
                    "max_output_tokens": 1024,
                    "temperature": 0.5,
                    "top_p": 0.8,
                    "top_k": 40
                }
        }
    }
        return model_list[feature_name]

    def getVertexModel(self, model_name: str):
        vertex_model = GenerativeModel(model_name)
        # if model_name == "text-bison-32k":
        #     vertex_model = Preview_TextGenerationModel.from_pretrained(model_name)
        # else:
        #     vertex_model = TextGenerationModel.from_pretrained(model_name)
        

        return vertex_model

    def generateMessageVertexAI(
            self, 
            input_prompt: str, 
            feature_name: str
        ) -> str:
        # get vertex parameter
        model = self.getModelAndParameter(feature_name)
        model_name = model["model"]
        # generation_config = model["parametor"]
        generation_config = {
            "max_output_tokens": 8192,
            "temperature": 1,
            "top_p": 0.95,
        }

        # Choose model between Preview and Stable Version
        vertex_model = self.getVertexModel(model_name)
        
        # result = vertex_model.predict(input_prompt, **model_parameter)
        result = vertex_model.generate_content([input_prompt], generation_config = generation_config)
        return result.text
    
    def claudeGennertor(self, input_prompt: str):
            message = self.anthropic_client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=4000,
            temperature=0.5,
            system="",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"{input_prompt}"
                        }
                    ]
                }
                ]
            )
            print(message.content)
            return message.content[0].text
    



