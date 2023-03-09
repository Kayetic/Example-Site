import openai
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

model_engine = "text-davinci-003"
prompt_text = "The CPU is"

response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt_text,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.7,
)

print(response.choices[0].text)
