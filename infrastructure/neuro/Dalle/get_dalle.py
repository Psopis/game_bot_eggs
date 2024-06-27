from gradio_client import Client
from deep_translator import GoogleTranslator


def get__dalle(prompt):
    translator = GoogleTranslator(source='ru', target='en')
    translation = translator.translate(prompt)
    client = Client("prithivMLmods/DALLE-4K")
    result = client.predict(
        prompt=translation,
        negative_prompt="(deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, (mutated hands and fingers:1.4), disconnected limbs, mutation, mutated, ugly, disgusting, blurry, amputation",
        use_negative_prompt=True,
        style="3840 x 2160",
        seed=0,
        width=1024,
        height=1024,
        guidance_scale=6,
        randomize_seed=True,
        api_name="/run"
    )
    return result[0]
