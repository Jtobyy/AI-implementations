from groq import Groq
from abc import ABC, abstractmethod

import os

class AIClient(ABC):
    @abstractmethod
    def generate_response(self, prompt, model):
        pass

class GroqClient(AIClient):
    def __init__(self):
        # Initialize the Groq client with the API key
        self.client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )
    
    def generate_response(self, prompt, model="llama3-8b-8192"):
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=model,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            raise Exception(f"Failed to generate response: {str(e)}")

class OpenAIClient(AIClient):
    def __init__(self):
        # Initialize OpenAI with the API key
        openai.api_key = os.environ.get("OPENAI_API_KEY")
    
    def generate_response(self, prompt, model="gpt-3.5-turbo"):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ]
            )
            return response.choices[0].message['content']
        except Exception as e:
            raise Exception(f"Failed to generate response: {str(e)}")
