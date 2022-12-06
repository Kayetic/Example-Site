import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Explain hashing with an example",
    temperature=0,
    max_tokens=3000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response["choices"][0]["text"])
