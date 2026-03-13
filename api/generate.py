from flask import Flask, request, jsonify
from groq import Groq
import json, re, os

app = Flask(__name__)

TOPICS = [
    {"id": "oops",       "label": "OOPs & Classes"},
    {"id": "functions",  "label": "Functions & Lambdas"},
    {"id": "dsa",        "label": "Data Structures"},
    {"id": "exceptions", "label": "Exception Handling"},
    {"id": "generators", "label": "Generators & Iterators"},
    {"id": "fileio",     "label": "File I/O & OS"},
    {"id": "regex",      "label": "Regex & Strings"},
    {"id": "modules",    "label": "Modules & Packages"},
]

@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        data          = request.get_json(force=True, silent=True) or {}
        topic_id      = data.get('topic', 'oops')
        difficulty    = data.get('difficulty', 'medium')
        num_questions = min(int(data.get('num_questions', 5)), 15)

        topic_obj   = next((t for t in TOPICS if t['id'] == topic_id), TOPICS[0])
        topic_label = topic_obj['label']

        api_key = os.environ.get('GROQ_API_KEY')
        if not api_key:
            return jsonify({"success": False, "error": "API key not set"}), 500

        client = Groq(api_key=api_key)

        prompt = f"""Generate exactly {num_questions} {difficulty}-level MCQ questions on Python topic: {topic_label}.
Return ONLY a valid JSON array, no markdown, no extra text:
[
  {{
    "question": "Question?",
    "code": "",
    "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
    "answer": "A",
    "explanation": "Why A is correct."
  }}
]"""

        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
        )
        raw   = chat_completion.choices[0].message.content.strip()
        match = re.search(r'\[.*\]', raw, re.DOTALL)
        if match:
            questions = json.loads(match.group())
            return jsonify({"success": True, "questions": questions, "topic": topic_label, "difficulty": difficulty})
        else:
            return jsonify({"success": False, "error": "Could not parse response"}), 500

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
