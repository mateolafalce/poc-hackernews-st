import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


def make_yt_cinema(yt_script: str) -> str:
    client = OpenAI(api_key=api_key)
    
    prompt = f"""Based on the following YouTube Short script, I need you to generate cinematic scene descriptions for each phrase or sentence. These descriptions will be used to generate video with Sora AI.

IMPORTANT REQUIREMENTS:
- NO person should appear narrating or speaking on camera
- ALL text is voice-over only
- Each scene should be visually compelling and dynamic
- Descriptions should be optimized for Sora video generation (clear, specific, cinematic)
- Focus on visual storytelling that complements the narration

Please format your response EXACTLY as follows:
[Script phrase or sentence] - [Detailed cinematic description of the scene]

For example:
"Welcome to the future of JavaScript" - Wide aerial shot of a futuristic tech campus at golden hour, with sleek glass buildings reflecting the sunset, camera slowly descending towards the main entrance

Script to analyze:
{yt_script}

Generate the cinematic descriptions:"""
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert cinematographer and visual storyteller specialized in creating compelling scene descriptions for AI video generation, particularly for Sora. You understand how to translate narrative into powerful visual sequences."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.8,
            max_tokens=1000
        )
        
        cinema_descriptions = response.choices[0].message.content
        return cinema_descriptions
        
    except Exception as e:
        print(f"Error al generar descripciones cinemáticas: {e}")
        return None
