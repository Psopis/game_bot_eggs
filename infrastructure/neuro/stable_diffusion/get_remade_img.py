import requests
from gradio_client import Client
from deep_translator import GoogleTranslator


def get_SD_picture(prompt):
    translator = GoogleTranslator(source='ru', target='en')
    translation = translator.translate(prompt)

    client = Client("stabilityai/stable-diffusion-3-medium")

    result = client.predict(
        prompt=translation,
        negative_prompt="Hello!!",
        seed=0,
        randomize_seed=True,
        width=1024,
        height=1024,
        guidance_scale=5,
        num_inference_steps=28,
        api_name="/infer",

    )

    return result[0]
