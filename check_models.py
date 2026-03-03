import google.generativeai as genai
import os

# --- PASTE YOUR API KEY BELOW ---
api_key = "AIzaSyAqqzrPezlMeYFSLLMQRd1XPbXC4ifcexs"

genai.configure(api_key=api_key)

print("Searching for available models...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"FOUND: {m.name}")
except Exception as e:
    print(f"Error: {e}")