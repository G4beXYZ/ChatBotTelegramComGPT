import openai

openai.api_key = "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"
start_sequence = "\nA:"
restart_sequence = "\n\nQ: "
def generate_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer.",
        temperature=0.98,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop = ["\n"]
        )
    return response.choices[0].text.strip()

while True:
    user_input = input("\n")
    response = generate_response(user_input)
    print(response)