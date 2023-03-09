# Import the openai module
import openai

# Set your API key
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Create a chat completion object with your prompt
chat = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        # {"role": "system", "content": "You are a computer science expert."},
        {"role": "user", "content": "What is a CPU?"}
    ]
)

# Print the assistant's reply
print(chat["choices"][0]["message"]["content"])
