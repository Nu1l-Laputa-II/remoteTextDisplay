import requests
import time

def fetch_sentences():
    url = "https://raw.githubusercontent.com/Nu1l-Laputa-II/goldenSentence/main/sentence.md"
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text
        return [s.strip() for s in content.split('\n\n') if s.strip()]
    except Exception as e:
        print(f"Error fetching sentences: {e}")
        return []

def display_sentences():
    sentences = fetch_sentences()
    if not sentences:
        print("No sentences found or error occurred")
        return
    
    while True:
        for sentence in sentences:
            print(sentence)
            time.sleep(3)

if __name__ == "__main__":
    display_sentences()
