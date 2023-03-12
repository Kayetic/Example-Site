# Import the openai module
import openai

# Set your API key
openai.api_key = "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"

# open the three files and append them to one text variable

with open("response1.txt", "r") as f:
    response1 = f.read()
with open("response2.txt", "r") as f:
    response2 = f.read()
with open("response3.txt", "r") as f:
    response3 = f.read()

one_response = response1 + response2 + response3
# save the one_response variable to a text file
with open("one_response.txt", "w") as f:
    f.write(one_response)
