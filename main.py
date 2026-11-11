import os
import google.generativeai as genai

# 1. GitHub Secrets से API Key लेना
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

print("--- Jarvis Shorts Autopilot शुरू हो गया है ---")

if not GEMINI_API_KEY:
    print("एरर: GEMINI_API_KEY नहीं मिली!")
    exit(1)

try:
    # 2. सही और स्टेबल मॉडल कॉन्फिगर करना
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # 3. कंटेंट जनरेट करना
    prompt = "Write a catchy YouTube Short title and description about a cool science fact."
    response = model.generate_content(prompt)
    
    print("\n[AI जनरेटेड मेटाडाटा]:")
    print(response.text)
    print("\n--- स्क्रिप्ट सफलतापूर्वक पूरी हो गई है! ---")

except Exception as e:
    print(f"कनेक्शन में दिक्कत आई: {e}")
    exit(1)
