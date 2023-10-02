import json
import vertexai
from vertexai.preview.language_models import TextGenerationModel
from google.oauth2 import service_account
import os


def vertexGenerator(language, feature, tone, input_message):
    model_list = {
        "เขียนแคปชั่นขายของ": {
            "model": "text-bison@001",
            "parametor":
                {
                    "max_output_tokens": 1024,
                    "temperature": 0.6,
                    "top_p": 0.8,
                    "top_k": 40
                }
        },
        "ช่วยคิดคอนเทนต์": {
            "model": "text-bison@001",
            "parametor":
                {
                    "max_output_tokens": 1024,
                    "temperature": 0.2,
                    "top_p": 0.8,
                    "top_k": 40
                }
        },
        "เขียนบทความ": {
            "model": "text-bison-32k",
            "parametor":
                {
                    "max_output_tokens": 5500,
                    "temperature": 0.2,
                    "top_p": 0.8,
                    "top_k": 40
                }
        },
        "เขียนสคริปวิดีโอสั้น": {
            "model": "text-bison-32k",
            "parametor":
                {
                    "max_output_tokens": 6000,
                    "temperature": 0.4,
                    "top_p": 0.8,
                    "top_k": 40
                }
        },
        "เขียนประโยคเปิดคลิป": {
            "model":"text-bison@001",
            "parametor":
                {
                    "max_output_tokens": 1024,
                    "temperature": 0.5,
                    "top_p": 0.8,
                    "top_k": 40
                }
        }
    }
    prompt_list = {
        "th": {
            "เขียนแคปชั่นขายของ": """Write a social media announcement about [{input}] with hashtags and emojis The feeling of the message should be [{type}]. [เป็นภาษาไทยเท่านั้น]""",
            "ช่วยคิดคอนเทนต์": """Create list of idea content with short biref about [ {input}] that all content should make feeling like [ {type}] show list of idea with short biref [เป็นภาษาไทยเท่านั้น]:""",
            "เขียนบทความ": """Write a blog post with high demand SED keyword that talks about [{input}] that article should feel like [{type}] [เป็นภาษาไทยเท่านั้น]:""",
            "เขียนสคริปวิดีโอสั้น": """write full scripts for short video that talk about [ {input}] and the feeling of scripts is [ {type}] [เป็นภาษาไทยเท่านั้น]:""",
            "เขียนประโยคเปิดคลิป": """Write a captivating clickbait sentence for opening a short video to talk about [ {input}] and feeling of sentence should be [ {type}] The sentence that instantly grabs viewer's attention and sets the stage for an unforgettable experience [เป็นภาษาไทยเท่านั้น]""",
        },
        "eng": {
            "เขียนแคปชั่นขายของ": "Write a social media announcement about [ {input}] and the feeling of message is [ {type}]:",
            "ช่วยคิดคอนเทนต์": """Create list of idea content with short biref about [ {input}] that all content should make feeling like [ {type}] show list of idea with short biref """,
            "เขียนบทความ": "Write a blog post with high demand SED keyword that talks about [{input}] that article should feel like [{type}]",
            "เขียนสคริปวิดีโอสั้น": "write full scripts for short video that talk about [ {input}] and the feeling of scripts is [ {type}]",
            "เขียนประโยคเปิดคลิป": """Write a captivating clickbait sentence for opening a short video to talk about [ {input}] and feeling of sentence should be [ {type}] The sentence that instantly grabs viewer's attention and sets the stage for an unforgettable experience""",
        },
        "id": {
            "เขียนแคปชั่นขายของ": "Write a social media announcement about [ {input}] and the feeling of message is [ {type}] [in Bahasa Indonesia Only]:",
            "ช่วยคิดคอนเทนต์": """Create list of idea content with short biref about [ {input}] that all content should make feeling like [ {type}] 
        show list of idea with short biref [in Bahasa Indonesia Only]:""",
            "เขียนบทความ": "Write a blog post with high demand SED keyword that talks about [ {input}] that article should feel like [ {type}] in [Bahasa Indonesia]:",
            "เขียนสคริปวิดีโอสั้น": "write full scripts for short video that talk about [ {input}] and the feeling of scripts is [ {type}] [in Bahasa Indonesia Only]:",
            "เขียนประโยคเปิดคลิป": """Write a captivating clickbait sentence for opening a short video to talk about [ {input}] and feeling of sentence should be [ {type}] The sentence that instantly grabs viewer's attention and sets the stage for an unforgettable experience [in Bahasa Indonesia Only]""",
        },
    }
    credential = service_account.Credentials.from_service_account_file("gcp_sa_key.json")
    vertexai.init(project=os.environ.get("GCP_PROJECT_ID"), location="us-central1", credentials=credential)
    vertex_model = TextGenerationModel.from_pretrained(model_list[feature]["model"])
    parametor = model_list[feature]["parametor"]
    prompt = prompt_list[language][feature]
    prompt = prompt.format(
        input = input_message,
        type = tone
    )
    print(prompt)
    resp = vertex_model.predict(prompt, **parametor)

    return resp.text
    
