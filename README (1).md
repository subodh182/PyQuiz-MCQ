# 🐍 PyQuiz AI — AI-Powered Python MCQ Generator

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?style=for-the-badge&logo=flask)
![Groq](https://img.shields.io/badge/Groq-Llama_3.3_70B-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> Generate unlimited Python MCQ quizzes instantly using AI. Built with Flask + Groq's ultra-fast Llama 3.3 70B inference.

---

## 📸 Preview

```
🐍 PyQuiz
├── 8 Python Topics
├── 3 Difficulty Levels  
├── Up to 15 Questions
└── Instant AI Generation (<2 seconds)
```

---

## ✨ Features

- ⚡ **AI-Powered** — Llama 3.3 70B generates unique questions every time
- 🎯 **8 Topics** — OOPs, Functions, DSA, Exceptions, Generators, File I/O, Regex, Modules
- 🎚️ **3 Difficulty Levels** — Easy, Medium, Hard
- 💡 **Explanations** — Every question has a detailed explanation
- 📊 **Live Score Tracker** — Real-time progress bar and score
- 🏆 **Results Screen** — Animated SVG score ring with performance feedback
- 💻 **Code Snippets** — Questions include Python code blocks where relevant
- 🔁 **Retry / New Quiz** — Retry same quiz or generate a fresh one
- 📱 **Fully Responsive** — Works on mobile, tablet, desktop

---

## 🗂️ Project Structure

```
online-quiz/
│
├── app.py                  # Flask backend + Groq API integration
├── requirements.txt        # Python dependencies
├── README.md               # You are here!
│
├── templates/
│   └── index.html          # Full frontend (HTML + CSS + JS)
│
└── venv/                   # Virtual environment (auto-generated)
```

---

## 🛠️ Tech Stack

| Layer      | Technology              |
|------------|-------------------------|
| Backend    | Python, Flask           |
| AI Model   | Llama 3.3 70B (via Groq)|
| Frontend   | HTML5, CSS3, Vanilla JS |
| Fonts      | Outfit, JetBrains Mono  |
| Animations | CSS Keyframes, Canvas   |

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/pyquiz-ai.git
cd pyquiz-ai
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Add Your Groq API Key

Open `app.py` and replace the API key:
```python
API_KEY = 'your_groq_api_key_here'
```

> 🔑 Get your free API key at: https://console.groq.com

### 6. Run the App
```bash
python app.py
```

### 7. Open in Browser
```
http://localhost:5000
```

---

## 📋 Requirements

```
flask==3.0.0
groq==0.4.2
```

---

## 🎮 How to Use

1. **Select a Topic** — Click on any of the 8 Python topic cards
2. **Set Difficulty** — Choose Easy, Medium, or Hard
3. **Choose Count** — Drag slider to pick 3–15 questions
4. **Generate** — Click "Generate Quiz" button
5. **Answer** — Click on your answer for each question
6. **Review** — See explanations after each answer
7. **Results** — View your final score with performance feedback

---

## 📚 Available Topics

| Icon | Topic               | Covers                                  |
|------|---------------------|-----------------------------------------|
| 🧬   | OOPs & Classes      | Inheritance, Polymorphism, Encapsulation|
| ⚡   | Functions & Lambdas | Args, Decorators, Closures              |
| 🗂️  | Data Structures     | Lists, Dicts, Sets, Tuples              |
| 🛡️  | Exception Handling  | Try/Except, Custom Errors               |
| ♾️   | Generators          | Yield, Lazy Evaluation, Iterators       |
| 📁   | File I/O & OS       | Read, Write, Path operations            |
| 🔍   | Regex & Strings     | Pattern matching, String methods        |
| 📦   | Modules & Packages  | Import, __init__, pip packages          |

---

## 🚀 Future Features (Roadmap)

- [ ] ⏱️ Timer per question with auto-submit
- [ ] 👤 User Login & Registration
- [ ] 🏆 Global Leaderboard
- [ ] 📊 Analytics Dashboard & Quiz History
- [ ] 📄 PDF Result Card Download
- [ ] 🎮 Lives System & Hints (50/50 lifeline)
- [ ] 🌙 Dark/Light Mode Toggle
- [ ] 🔊 Sound Effects
- [ ] 📱 Share Score on WhatsApp/Twitter
- [ ] 🌐 Hindi + English Language Support
- [ ] ✍️ Custom Topic Input
- [ ] 🔖 Question Bookmarking

---

## 🔑 Environment Variables (Optional)

Instead of hardcoding the API key, you can use a `.env` file:

```bash
pip install python-dotenv
```

Create `.env` file:
```
GROQ_API_KEY=your_key_here
```

Update `app.py`:
```python
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv('GROQ_API_KEY')
```

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Made with ❤️ using Flask + Groq AI

> ⭐ **Star this repo** if you found it helpful!
