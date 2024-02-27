import openai

openai.api_key = "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"
# openai.Model.list()

response = openai.Completion.create(
    engine="davinci",
    prompt="Translate the following English text to French: 'Hello, world.'",
    max_tokens=50,
)

print(response.choices[0].text)
