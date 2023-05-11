import openai
openai.api_key = "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"

def ask_gpt(prompt):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      temperature=0.5,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    message = response.choices[0].text.strip()
    return message

while True:
    user_input = input("You: ")
    bot_response = ask_gpt(user_input)
    print("Bot:", bot_response)
