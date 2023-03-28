import openai

# Set your API key
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

user_message = input("You: ")
# Create a chat completion object with your prompt
chat = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a very knowledgeable large language model that answers questions and says nothing else."},
        {"role": "user", "content": f"{user_message}"}
    ],
    max_tokens=8192)
