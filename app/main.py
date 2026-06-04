import os
from openai import OpenAI
from dotenv import load_dotenv

# Loading environment variables from a .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generateImg(text, sz):
    # Creating an image using given prompt text and image size
    img = client.images.generate(
        model="dall-e-3",
        prompt=text,
        n=1,
        size=sz
    )

    return img.data[0].url
