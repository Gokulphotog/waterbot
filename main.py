from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import random

app = FastAPI()

# Mount static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Chatbot responses with multiple natural conversation styles
conversation_flow = {
    "hello": [
        "Hi there! How are you feeling today?",
        "Hello! Need some hydration tips?",
        "Hey! What's up? Staying hydrated?"
    ],
    "how are you": [
        "I'm just a bot, but I'm always hydrated! What about you?",
        "Feeling great! Have you had water today?",
        "I'm good! Are you keeping up with your water intake?"
    ],
    "how much water should i drink": [
        "A healthy adult should drink at least 2-3 liters daily. How much do you usually drink?",
        "It depends on your body weight and activity. Generally, 8-10 glasses a day is good.",
        "Everyone's needs are different, but 2-4 liters per day is ideal."
    ],
    "benefits of drinking water": [
        "Water helps digestion, boosts energy, and keeps your skin fresh!",
        "Drinking enough water improves brain function and prevents headaches.",
        "Hydration helps with detoxification and keeps your organs healthy!"
    ],
    "symptoms of dehydration": [
        "Common signs include headaches, dizziness, dry mouth, and fatigue. Are you feeling any of these?",
        "If your urine is dark yellow, you might be dehydrated! Drink a glass of water now.",
        "Dehydration can cause low energy, dry skin, and muscle cramps."
    ],
    "remind me to drink water": [
        "Sure! I'll remind you every 2 hours. Just keep a bottle nearby!",
        "Stay hydrated! Maybe set alarms on your phone as a reminder?",
        "Drinking water regularly is a great habit! Do you want daily reminders?"
    ],
    "bye": [
        "Goodbye! Stay hydrated and take care. 💧",
        "See you later! Don't forget your water intake.",
        "Bye! Drink a glass of water before you go!"
    ]
}

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/chat/{query}")
def chat(query: str):
    query = query.lower()
    for key in conversation_flow:
        if key in query:
            return {"response": random.choice(conversation_flow[key])}

    return {"response": "Hmm, I don't know about that. But drinking water is always a good idea! 💧"}
