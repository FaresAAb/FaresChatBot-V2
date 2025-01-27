# 🚀 Fares's AI ChatBot

A powerful AI chatbot using **Langchain Ollama** with a **Flask API**, **command-line interface**, **web-based UI**, and **speech recognition** for voice input/output.

## 📌 Features

- **Flask API** to handle HTTP requests.
- **Command-line chatbot** for local interaction.
- **Web UI** for easy access via browser.
- **Speech Recognition & Text-to-Speech** for voice-based conversations.
- **Context-aware responses** (maintains conversation history).
- **Logging system** to store chat history.

---

## 🛠 Installation & Setup

### 1️⃣ Install Python
Ensure you have **Python 3.10+** installed:

```sh
python --version
```

If not installed, download Python from [python.org](https://www.python.org/downloads/).

### 2️⃣ Clone the Repository

```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/FaresChatBot.git
cd FaresChatBot
```

### 3️⃣ Set Up a Virtual Environment

```sh
python -m venv env
```
Activate the virtual environment:

#### Windows:
```sh
./env/Scripts/activate
```

#### Mac/Linux:
```sh
source env/bin/activate
```

### 4️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```
Create a `requirements.txt` file with:

```
flask
flask-cors
langchain_ollama
SpeechRecognition
pyttsx3
pyaudio
```

---

## 🚀 Running the ChatBot

### Run Flask API (`app.py`)

```sh
python app.py
```
- Flask will start the server on `http://127.0.0.1:5000`
- Test with **Postman** or **curl**:
  ```sh
  curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"message": "Hello!"}'
  ```
- Open the **Web UI** in a browser:
  ```
  http://127.0.0.1:5000/
  ```

### Run Command-Line Chatbot (`chatbot.py`) with Speech Recognition

```sh
python chatbot.py
```
- Type `s` for **speech mode** (voice input & output).
- Type `t` for **text mode** (manual typing).
- Type `exit` to quit.

---

## 🎤 Speech Recognition & Text-to-Speech

### Installation
Ensure you have installed the required dependencies:

```sh
pip install SpeechRecognition pyttsx3 pyaudio
```

### Speech Recognition & Text-to-Speech Code

```python
import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening... Speak now")
        recognizer.adjust_for_ambient_noise(source, duration=1.5)
        try:
            audio = recognizer.listen(source, timeout=5)
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError:
            return "Speech recognition service unavailable."
```

---

## 🖥️ Web UI Setup & Instructions

### Folder Structure

```
FaresChat/
│── env/             (Virtual environment)
│── app.py           ✅ Flask backend
│── chatbot.py       ✅ Chatbot script
│── templates/       ✅ HTML frontend
│   └── index.html   ✅ Chatbot UI
```

### `index.html` Code (Frontend UI)

Located in `templates/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI ChatBot</title>
</head>
<body>
    <div>
        <h2>AI ChatBot</h2>
        <div id="chat-box"></div>
        <input type="text" id="user-input" placeholder="Type a message...">
        <button onclick="sendMessage()">Send</button>
    </div>
    <script>
        async function sendMessage() {
            let userInput = document.getElementById("user-input").value;
            if (!userInput.trim()) return;
            let response = await fetch("/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: userInput })
            });
            let data = await response.json();
            document.getElementById("chat-box").innerHTML += `<p><b>You:</b> ${userInput}</p><p><b>Bot:</b> ${data.response}</p>`;
            document.getElementById("user-input").value = "";
        }
    </script>
</body>
</html>
```

---

## 📡 Deploying the Flask API

### Deploy with Gunicorn (Linux Server)

```sh
pip install gunicorn
```

Run Flask with Gunicorn:

```sh
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## 📝 License

This project is open-source and free to use!

---

## 📩 Contact

For any questions, contact **Fares** via email or open an issue on GitHub!

---

**Enjoy your AI-powered chatbot! 🚀🔥**

