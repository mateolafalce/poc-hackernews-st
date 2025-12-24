import requests
from db import article_exists

def sanitize_filename(title):
    import re
    filename = re.sub(r'[^\w\s-]', '', title)
    filename = re.sub(r'\s+', '_', filename)
    return filename[:100]

def get_article_html(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error getting HTML: {e}")
        return None

def get_top_story():
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(url)
    response.raise_for_status()
    story_ids = response.json()
    
    for story_id in story_ids:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story_response = requests.get(story_url)
        story_response.raise_for_status()
        story_data = story_response.json()
        
        if story_data.get("type") == "story":
            title = story_data.get("title", "")
            
            if not article_exists(title):
                print(f"New article found: {title}")
                
                article_url = story_data.get("url")
                
                if article_url:
                    html_content = get_article_html(article_url)
                    
                    if html_content:
                        story_data['html_content'] = html_content
                        story_data['html_filepath'] = None
                        return story_data
                    else:
                        print(f"Could not get article HTML, trying next one...")
                        continue
                else:
                    print(f"Article has no external URL, trying next one...")
                    continue
            else:
                print(f"Article already exists in DB, skipping: {title}")

    return None
