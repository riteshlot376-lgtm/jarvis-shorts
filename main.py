import os
import google.generativeai as genai

# 1. गिटहब के सीक्रेट से की उठाना
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("एरर: GEMINI_API_KEY नहीं मिली!")
    exit(1)

# 2. जेमिनी को सेट करना
genai.configure(api_key=api_key)

# 3. हिंदी में वायरल शॉर्ट्स का टाइटल और डिस्क्रिप्शन जनरेट करना
model = genai.GenerativeModel('gemini-1.5-flash')
prompt = "विज्ञान के किसी बहुत ही रोचक और चौका देने वाले रहस्य पर एक YouTube Short के लिए आकर्षक हिंदी टाइटल, शानदार डिस्क्रिप्शन और वायरल हैशटैग लिखो।"

response = model.generate_content(prompt)

print("--- हिंदी में फाइनल रिजल्ट आ गया है ---")
print(response.text)
