import os
import json
from datetime import datetime
from yt_content import make_yt_content
from cinema import make_yt_cinema
from sora import make_yt_video


def main():
    # Save the LLM response to articles_html as JSON
    if yt_content:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = os.path.join(os.path.dirname(__file__), '..', 'articles_html', f'yt_script_{timestamp}.json')
        with open(output_path, 'w', encoding='utf-8') as f:
            # Parse the JSON string and save it with proper formatting
            json_data = json.loads(yt_content)
            json.dump(json_data, f, ensure_ascii=False, indent=2)

    # Load the YouTube script from content.txt
    content_path = os.path.join(os.path.dirname(__file__), '..', 'articles_html', 'yt_script.json')
    with open(content_path, 'r', encoding='utf-8') as f:
        yt_script = json.load(f)
    


    # make the audio for the video (ElevenLabs)
    #yt_audio = make_yt_audio(yt_content)
    
    # make some cinematic for the video (GPT 4.1)
    #yt_cinema = make_yt_cinema(yt_script)
    
    #if yt_cinema:
    #    print("Descripciones cinemáticas generadas:")
    #    print(yt_cinema)
    #    print("\n" + "="*80 + "\n")
        
        # Save cinema descriptions
        #timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        #cinema_path = os.path.join(os.path.dirname(__file__), '..', 'articles_html', f'cinema_{timestamp}.txt')
        #with open(cinema_path, 'w', encoding='utf-8') as f:
        #    f.write(yt_cinema)
        #print(f"Descripciones cinemáticas guardadas en: {cinema_path}")

    
    # make some video for youtube (Sora)
    prompt = "Hey Bay Area tech heads!"
    description = "Dynamic time-lapse of the San Francisco skyline at dawn, the iconic Golden Gate Bridge emerging through morning mist, with subtle digital data streams overlay to evoke tech innovation."
    
    yt_video = make_yt_video(prompt, description) # $0.8 for 4 sec ?? LOL
    
    if yt_video:
        print(f"\n✓ Video generado y guardado exitosamente!")
    else:
        print(f"\n✗ Error al generar el video")

    
    # upload the video to youtube (YT API)
    #upload_yt_video(yt_video)


if __name__ == "__main__":
    main()
