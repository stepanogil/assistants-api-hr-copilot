
from openai import OpenAI
client = OpenAI()

def extract_ocr(user_prompt, urls):
    """
    Extracts text from images using OpenAI's GPT-4 Vision API.
    """    
    image_url_messages = [
        {
            "type": "image_url",
            "image_url": {
                "url": url,
            },
        }
        for url in urls
    ]

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": user_prompt,
                    }
                ] + image_url_messages
            }
        ],
        max_tokens=300,
    )
    return response.choices[0].message.content

