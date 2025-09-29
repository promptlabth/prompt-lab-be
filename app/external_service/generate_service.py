import openai
import os
import json
import requests
import anthropic
from google.oauth2 import service_account

class GenerateService:
    def __init__(self) -> None:
        openai.api_key = os.environ.get("OPENAI_KEY")
        self.gemini_api_key = os.environ.get("GEMINI_API_KEY")
        self.anthropic_client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    def generateMessageOpenAI(self, input_prompt: str):
        result = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": input_prompt},
            ]
        )
        assistant_reply = result['choices'][0]['message']['content']
        return assistant_reply

    def generateMessageGemini(self, input_prompt: str) -> str:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={self.gemini_api_key}"
        
        headers = {
            'Content-Type': 'application/json'
        }
        
        payload = {
            "contents": [{
                "parts": [{"text": input_prompt}]
            }]
        }
        
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        result = response.json()
        return result['candidates'][0]['content']['parts'][0]['text']

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



