import openai

openai.api_key = "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"

prompt = "Hello"
baseMessages = [
    {"role": "system", "content": "You are an assistant that will answer questions."},
    {"role": "user", "content": f"{prompt}"}
]


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
