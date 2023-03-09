<<<<<<< HEAD
# Import the openai module
import openai
=======
import openai

openai.api_key = "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"

prompt = "Hello"
baseMessages = [
    {"role": "system", "content": "You are an assistant that will answer questions."},
    {"role": "user", "content": f"{prompt}"}
]
>>>>>>> 0efe665c119950743cf3b732a9e4d5904265b1b5

# Set your API key
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

<<<<<<< HEAD
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
=======
def callGPT():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=baseMessages,
    )
    return response


while True:

    userInput = input("Enter query: ")
    response = callGPT(userInput)
    print(response['choices'][0]['message']['content'])
    gptResponse = response['choices'][0]['message']['content']
    baseMessages.append({"role": "assistant", "content": f"{gptResponse}"})
>>>>>>> 0efe665c119950743cf3b732a9e4d5904265b1b5
