from flask import Flask, render_template, request, jsonify
from groq import Groq
import json, re
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv('GROQ_API_KEY')
client = Groq(api_key=API_KEY)

TOPICS = [
    {"id": "oops", "label": "OOPs & Classes", "icon": "🧬", "desc": "Inheritance, Polymorphism, Encapsulation"},
    {"id": "functions", "label": "Functions & Lambdas", "icon": "⚡", "desc": "Args, Decorators, Closures"},
    {"id": "dsa", "label": "Data Structures", "icon": "🗂️", "desc": "Lists, Dicts, Sets, Tuples"},
    {"id": "exceptions", "label": "Exception Handling", "icon": "🛡️", "desc": "Try/Except, Custom Errors"},
    {"id": "generators", "label": "Generators & Iterators", "icon": "♾️", "desc": "Yield, Lazy Evaluation"},
    {"id": "fileio", "label": "File I/O & OS", "icon": "📁", "desc": "Read, Write, Path operations"},
    {"id": "regex", "label": "Regex & Strings", "icon": "🔍", "desc": "Pattern matching, String methods"},
    {"id": "modules", "label": "Modules & Packages", "icon": "📦", "desc": "Import, __init__, pip packages"},
]

DIFFICULTIES = [
    {"id": "easy", "label": "Easy", "color": "#4ade80"},
    {"id": "medium", "label": "Medium", "color": "#fb923c"},
    {"id": "hard", "label": "Hard", "color": "#f87171"},
]

@app.route('/')
def index():
    return render_template('index.html', topics=TOPICS, difficulties=DIFFICULTIES)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    topic_id = data.get('topic', 'oops')
    difficulty = data.get('difficulty', 'medium')
    num_questions = min(int(data.get('num_questions', 5)), 15)

    topic_obj = next((t for t in TOPICS if t['id'] == topic_id), TOPICS[0])
    topic_label = topic_obj['label']

    prompt = f"""Generate exactly {num_questions} {difficulty}-level MCQ questions on Python topic: {topic_label}.

Return ONLY a valid JSON array. No markdown, no explanation, just raw JSON:
[
  {{
    "question": "Question text?",
    "code": "optional_code_snippet_or_empty_string",
    "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
    "answer": "A",
    "explanation": "Why A is correct."
  }}
]

Rules:
- Include a short code snippet in "code" field when relevant (Python code), else leave as ""
- Make distractors plausible
- Vary question styles (what outputs, what error, fill in blank, etc.)
"""

    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
        )
        raw = chat_completion.choices[0].message.content.strip()
        match = re.search(r'\[.*\]', raw, re.DOTALL)
        if match:
            questions = json.loads(match.group())
            return jsonify({"success": True, "questions": questions, "topic": topic_label, "difficulty": difficulty})
        else:
            return jsonify({"success": False, "error": "Could not parse AI response"}), 500
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)