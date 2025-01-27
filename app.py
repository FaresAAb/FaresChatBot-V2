from flask import Flask, request, jsonify
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)

# Define conversation model
template = """
You are a helpful and knowledgeable assistant. Answer the question clearly and concisely.
Here is the Conversation History:
{context}

Question: {question}
Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

conversation_history = []

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({"error": "Empty message"}), 400

    try:
        context = "\n".join(conversation_history[-5:])  # Keep last 5 messages
        result = chain.invoke({"context": context, "question": user_input})
        
        # Store conversation history
        conversation_history.append(f"User: {user_input}\nAI: {result}")

        return jsonify({"response": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
