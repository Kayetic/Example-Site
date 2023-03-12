# Import the openai module
import openai

# Set your API key
openai.api_key = "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"

user_message = input("You: ")
# Create a chat completion object with your prompt
chat = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a computer science expert that writes in a fairly human-sounding fashion."},
        {"role": "user", "content": f"{user_message}"}
    ],
    temperature=0.86,
    n=3,
    top_p=1,
    frequency_penalty=1.73,
    presence_penalty=0.89
)

# Print the assistant's reply
# print(chat["choices"][0]["message"]["content"])
# print(chat["choices"][0]["message"]["content"])
# print(chat["choices"][1]["message"]["content"])
# print(chat["choices"][2]["message"]["content"])

# save each response to a separete text file
with open("response1.txt", "w") as f:
    f.write(chat["choices"][0]["message"]["content"])
with open("response2.txt", "w") as f:
    f.write(chat["choices"][1]["message"]["content"])
with open("response3.txt", "w") as f:
    f.write(chat["choices"][2]["message"]["content"])

# load those three files into a new chat request with the same paramters but with the user's prompt as: "Condense these three responses into one response that is the best of the three responses." and then print the response.

# condense the three variabeles into one variable that contains the three responses
one_response = chat["choices"][0]["message"]["content"] + chat["choices"][1]["message"]["content"] + chat["choices"][2]["message"]["content"]
print(one_response)

# Create a chat completion object with your prompt
chat = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a computer science expert that writes in a fairly human-sounding fashion."},
        {"role": "user", "content": "Condense these three responses into one response that is the best of the three responses."}
    ],
    temperature=0.86,
    top_p=1,
    frequency_penalty=1.73,
    presence_penalty=0.89
)
