import openai

openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxx"

# open the three files and append them to one text variable

with open("response1.txt", "r") as f:
    response1 = f.read()
with open("response2.txt", "r") as f:
    response2 = f.read()
with open("response3.txt", "r") as f:
    response3 = f.read()

one_response = f"\nResponse 1:\n{response1}\n\nResponse 2:\n{response2}\n\nResponse 3:\n{response3}"


def condense_responses():
    openai.api_key = "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"
    # Create a chat completion object with your prompt
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a writing expert that condenses three responses into one medium-length response. You will write in a compelling and creative tone that sounds like it was written by a human. You can also add your own information if necessary about the topic."},
            {"role": "user", "content": f"Condense this: {one_response}"},
        ],
        temperature=0.7,
        top_p=1,
        frequency_penalty=1.73,
        presence_penalty=0.89
    )
    return chat["choices"][0]["message"]["content"]


print("\n" * 5)
print(condense_responses())
