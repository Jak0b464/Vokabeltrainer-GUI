import os
import requests
import json
from dotenv import load_dotenv

# Lade die Umgebungsvariablen aus der .env Datei
load_dotenv("C:/Users/Jakob/OneDrive/Dokumenty/python/Tokens-env/.env")

# API-Schlüssel abrufen
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("Fehler: API-Schlüssel nicht gefunden!")
    exit()

# 📌 Bild-URL oder lokales Bild angeben
image_path = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Menu-card.jpg/800px-Menu-card.jpg"

# 📌 Vision API-Endpunkt
url = f"https://vision.googleapis.com/v1/images:annotate?key={api_key}"

# 📌 JSON-Anfrage für die API
headers = {"Content-Type": "application/json"}
data = {
    "requests": [
        {
            "image": {"source": {"imageUri": image_path}},
            "features": [{"type": "TEXT_DETECTION"}],
        }
    ]
}

# 📌 Anfrage an die API senden
response = requests.post(url, json=data, headers=headers)

# 📌 Ergebnis ausgeben
result = response.json()
print(json.dumps(result, indent=2, ensure_ascii=False))
