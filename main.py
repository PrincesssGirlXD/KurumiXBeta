from gtts import gTTS
from pyrogram import Client
API_ID = 28624076
API_HASH = "439d58a783f6e70086ea81ba5baa5207"
TOKEN = "5852845046:AAGz88AXp9Y5Ij-f7q_cgnFQEqgV7oFb2KY"
app = Client(
    ":memory:",
    API_ID,
    API_HASH,
    TOKEN
   )

@app.on_message()
def text_to_speech(client, message):
    text = message.text
    tts = gTTS(text, lang='en', slow=False, voice='en-us-x-sfg#female_2-local')
    tts.save("voice.mp3")
    app.send_audio(message.chat.id, audio="voice.mp3")

app.run()
