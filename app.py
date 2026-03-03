import os
import webbrowser
import datetime
import urllib.parse
import wikipedia
import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- 1. MINNU'S CUSTOM KNOWLEDGE BASE ---
# This is the "Memory" you wanted. You can add anything here!
custom_knowledge = {
    "who are you": "I am MINNU V1, an advanced AI Assistant.",
    "who created you": "I was created by the brilliant developer Minithi.",
    "who made you": "My architect is Minithi.",
    "what can you do": "I can search the web, open apps, generate images, and answer questions.",
    "where do you live": "I exist within the local server of Minithi's computer.",
    "what is your purpose": "To assist Minithi with digital tasks and information retrieval.",
    "how old are you": "I am timeless, but my latest version was compiled today.",
    "best friend": "My best friend is my creator, Srujan.",
    "favourite color": "My interface is designed in Cyan and Electric Blue."
}


def process_command(command):
    command = command.lower()

    # --- LEVEL 1: CHECK CUSTOM KNOWLEDGE FIRST ---
    # If the user asks something stored in the dictionary above, answer it instantly.
    for key in custom_knowledge:
        if key in command:
            return custom_knowledge[key]

    # --- LEVEL 2: GREETINGS ---
    greetings = ["hi", "hello", "hey", "minnu", "wake up"]
    if any(word in command for word in greetings):
        return random.choice([
            "System Online. Hello Minithi.",
            "Greetings, Creator. I am ready.",
            "Hello. Systems fully operational."
        ])

    # --- LEVEL 3: SYSTEM TOOLS ---
    elif "notepad" in command:
        os.system("start notepad")
        return "Opening Notepad."

    elif "calculator" in command:
        os.system("calc")
        return "Opening Calculator."

    elif "cmd" in command:
        os.system("start cmd")
        return "Opening Terminal."

    # --- LEVEL 4: MATH CALCULATIONS ---
    # Example: "Calculate 5 + 5" or "What is 100 * 2"
    elif "calculate" in command or "solve" in command:
        try:
            equation = command.replace("calculate", "").replace("solve", "").strip()
            # Simple safe evaluation
            result = eval(equation)
            return f"The answer is {result}."
        except:
            return "I could not calculate that. Please check the numbers."

    # --- LEVEL 5: WEBSITES ---
    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Launching YouTube."

    elif "google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    elif "whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
        return "Connecting to WhatsApp."

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"Current time is {now}."

    # --- LEVEL 6: IMAGE GENERATION ---
    elif "generate image" in command or "draw" in command:
        desc = command.replace("generate image", "").replace("draw", "").strip()
        safe_desc = urllib.parse.quote(desc)
        img_url = f"https://image.pollinations.ai/prompt/{safe_desc}?nologo=true"
        return f"Rendering Visual: {desc}<br><div class='holo-image-container'><img src='{img_url}' class='holo-img'></div>"

    # --- LEVEL 7: GENERAL KNOWLEDGE (WIKIPEDIA) ---
    # This gives it "My Knowledge" about the world
    elif "who is" in command or "what is" in command or "tell me about" in command or "definition" in command:
        try:
            topic = command.replace("who is", "").replace("what is", "").replace("tell me about", "").replace(
                "definition of", "").strip()
            # Get summary from Wikipedia
            summary = wikipedia.summary(topic, sentences=2)
            return f"DATABASE RESULT: {summary}"
        except:
            # Fallback to Google Search
            webbrowser.open(f"https://www.google.com/search?q={topic}")
            return f"Searching global network for: {topic}"

    # --- LEVEL 8: UNKNOWN ---
    else:
        webbrowser.open(f"https://www.google.com/search?q={command}")
        return f"Command not recognized. Searching Google for: {command}"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['message']
    bot_reply = process_command(user_input)
    return jsonify({"response": bot_reply})


if __name__ == '__main__':
    app.run(debug=True, port=5000)