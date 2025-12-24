import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


def make_yt_content(article_content: str) -> str:
    client = OpenAI(api_key=api_key)
    
    prompt = f"""Based on the following article, I want you to generate a brief YouTube Short video script of approximately 30 seconds or less. I want it to have a San Francisco Bay Area vibe and I want you to do it in American English. I don't want you to make any mention of subscribing at the end of the video.

Please format your response EXACTLY as follows:

- Title: [catchy title for the YouTube Short]
- Description: [brief description for the YouTube video]
- Script: [the actual video script, approximately 30 seconds when read aloud]

Article:
{article_content}"""
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a creative content creator specialized in making engaging YouTube Shorts scripts with a San Francisco Bay Area vibe."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        yt_script = response.choices[0].message.content
        return yt_script
        
    except Exception as e:
        print(f"Error generating YouTube content: {e}")
        return None

