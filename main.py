import os
import requests
import google.generativeai as genai

# 1. एनवायरनमेंट वेरिएबल्स से API Keys लेना
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

print("Jarvis Shorts Autopilot शुरू हो रहा है...")

# 2. Gemini AI को कॉन्फिगर करना (शॉर्ट्स स्क्रिप्ट और मेटाडाटा के लिए)
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # एआई से आकर्षक शॉर्ट्स टाइटल, डिस्क्रिप्शन और हैशटैग जनरेट कराना
    prompt = "Give a catchy YouTube Short title, a good description, and relevant tags including #Shorts, #YouTubeShorts for a viral AI facts video."
    response = model.generate_content(prompt)
    
    print("AI से जनरेटेड कंटेंट:")
    print(response.text)
else:
    print("चेतावनी: GEMINI_API_KEY नहीं मिली!")

# 3. ElevenLabs वॉयसओवर इंटीग्रेशन चेक
if ELEVENLABS_API_KEY:
    print("ElevenLabs API Key मिल गई है, वॉयसओवर तैयार किया जा रहा है...")
else:
    print("चेतावनी: ELEVENLABS_API_KEY नहीं मिली!")

print("ऑटोमेशन स्क्रिप्ट सफलतापूर्वक रन हो गई है!")
