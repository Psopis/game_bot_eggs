from openai import OpenAI

GOOGLE_API_KEY = 'AIzaSyBYRwKV-1Y_dvY925oey2Y1VN9EUwwVcjg'
OPENAI_BASE_URL = 'https://my-openai-gemini-omega.vercel.app/v1/'

client = OpenAI(
    api_key=GOOGLE_API_KEY,
    base_url=OPENAI_BASE_URL
)


def gpt_answer(message):
    chat_completion = client.chat.completions.create(
        messages=message,
        model="gemini",
    )
    return chat_completion.choices[0].message.content
