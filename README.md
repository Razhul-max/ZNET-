🤖 ZNET — Local AI Chat App (Streamlit + Ollama)
ZNET is a lightweight and fast AI chat interface built using Streamlit and Ollama.  
It allows you to run LLMs locally on your system with real-time streaming responses.

---

## ✨ Features
- ⚡ Local LLM chat using Ollama  
- 🎨 Clean Streamlit UI  
- 🔄 Real-time message streaming  
- 🔧 Easy model switching  
- 💬 Chat history stored in session  

---

## 📦 Requirements

Make sure you have:

- Python 3.9+
- Streamlit
- Ollama installed locally  
  👉 Install Ollama: https://ollama.com/download

---

## 🔧 Installation

 Install Python dependencies

pip install streamlit ollama

 Pull the required models (optional)

ollama pull qwen2.5:0.5b
ollama pull qwen2.5-coder:1.5b


---

🚀 Run the App

streamlit run app.py

App will start at:

http://localhost:8501


---

🧠 Supported Models

ZNET includes two small, fast models:

qwen2.5:0.5b

qwen2.5-coder:1.5b


You can add more models by editing the models list in the code.

⚠️ Deployment Note

ZNET cannot be deployed on Vercel or Streamlit Cloud, because:

Ollama requires a local machine or a custom server

Cloud-free hosting platforms do not support Ollama runtime


To deploy online, use:

AWS EC2

Google Cloud VM

DigitalOcean Droplet

Any VPS with Ollama installed



---

🤝 Contributing

Pull requests are welcome.
Feel free to open issues for improvements or bugs.


---

📄 License

MIT License
