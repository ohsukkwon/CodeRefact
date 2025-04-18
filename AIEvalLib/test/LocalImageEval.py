import base64
from openai import OpenAI

client = OpenAI()

# Function to encode the image
def encode_image(arg_image_path):
    with open(arg_image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# Path to your image
__image_path = "res/5.jpg"

# Getting the base64 string
base64_image = encode_image(__image_path)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "이미지에 대해 상세히 설명해줘.",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ],
        }
    ],
)

print(response.choices[0])