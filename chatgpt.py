import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

while True:

    prompt = input("\nIntroduce una pregunta: ")

    if prompt == "exit":
        break

    completion = openai.Completion.create(engine="text-davinci-003", 
                         prompt=prompt,
                         n=1,
                         max_tokens=2048)

    print(completion.choices[0].text)