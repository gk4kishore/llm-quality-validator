import requests

OLLAMA_URL = "http://localhost:11434"

def generate(prompt, model="llama3.2:1b", **options):
    resp = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={"model": model, "prompt": prompt, "stream": False, "options": options},
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()

