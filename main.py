import os
import requests
import json

# 1. सीक्रेट से की उठाना
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("एरर: GEMINI_API_KEY नहीं मिली!")
    exit(1)

print("--- Jarvis Shorts Autopilot नए तरीके से शुरू हो गया है ---")

# 2. सीधा गूगल के API सर्वर पर रिक्वेस्ट भेजना (बिना किसी भारी लाइब्रेरी के)
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

headers = {
    "Content-Type": "application/json"
}

payload = {
    "contents": [{
        "parts": [{
            "text": "विज्ञान के किसी बहुत ही रोचक और चौका देने वाले रहस्य पर एक YouTube Short के लिए आकर्षक हिंदी टाइटल, शानदार डिस्क्रिप्शन और वायरल हैशटैग लिखो।"
        }]
    }]
}

try:
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        res_data = response.json()
        output_text = res_data['candidates'][0]['content']['parts'][0]['text']
        print("\n[सफलता! हिंदी में फाइनल रिजल्ट]:")
        print(output_text)
        print("\n--- काम सफलतापूर्वक पूरा हो गया है! ---")
    else:
        print(f"API एरर आया है: {response.status_code}")
        print(response.text)
        exit(1)

except Exception as e:
    print(f"कनेक्शन में दिक्कत आई: {e}")
    exit(1)
