import openai
import os

class Gpt:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def completion(self, prompt, temperature, model, max_tokens, frequency_penalty = 0, presence_penalty = 0):
        response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty)
        return response
