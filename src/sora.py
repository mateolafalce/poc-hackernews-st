import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


def make_yt_video(prompt: str, description: str) -> str:
    client = OpenAI(api_key=api_key)
    
    # Add pixel art specification to the prompt
    full_prompt = f"Pixel art style, retro 8-bit aesthetic, pixelated graphics: {description}. Voice-over text: '{prompt}'"

    
    print(f"Generating video with Sora...")
    print(f"Prompt: {full_prompt[:100]}...")
    
    try:
        # Create the video without audio
        video = client.videos.create(
            model="sora-2",
            prompt=full_prompt,
            size="720x1280",  # Vertical format 9:16 for YouTube Shorts
            audio=False,  # No audio
        )
        
        print(f"Video generation started: {video.id}")
        progress = getattr(video, 'progress', 0)
        
        # Poll the video status
        import time
        while video.status in ['in_progress', 'queued']:
            video = client.videos.retrieve(video.id)
            progress = getattr(video, 'progress', 0)
            
            # Progress bar
            bar_length = 30
            filled_length = int((progress / 100) * bar_length)
            bar = '=' * filled_length + '-' * (bar_length - filled_length)
            status_text = 'Queued' if video.status == 'queued' else 'Processing'
            
            print(f"\r{status_text}: [{bar}] {progress:.1f}%", end='', flush=True)
            
            time.sleep(2)
        
        # New line after the progress bar
        print()
        
        # Check if it failed
        if video.status == 'failed':
            print('Error: Video generation failed')
            return None
        
        print(f"Video generation completed: {video.id}")
        print("Downloading video content...")
        
        # Download the video content
        content_response = client.videos.download_content(video.id)
        
        # Read the binary content
        content = content_response.read()
        
        # Save the video in articles_html
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        video_filename = f"sora_video_{timestamp}.mp4"
        video_path = os.path.join(
            os.path.dirname(__file__), 
            '..', 
            'articles_html', 
            video_filename
        )
        
        with open(video_path, 'wb') as f:
            f.write(content)

        
        print(f"Video saved at: {video_path}")
        file_size = os.path.getsize(video_path) / (1024*1024)
        print(f"File size: {file_size:.2f} MB")
        
        return video_path
        
    except Exception as e:
        print(f"Error generating video with Sora: {e}")
        return None