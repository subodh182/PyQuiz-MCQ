from http.server import BaseHTTPRequestHandler
from groq import Groq
import json, re, os

TOPICS = {
    "oops":       "OOPs & Classes",
    "functions":  "Functions & Lambdas",
    "dsa":        "Data Structures",
    "exceptions": "Exception Handling",
    "generators": "Generators & Iterators",
    "fileio":     "File I/O & OS",
    "regex":      "Regex & Strings",
    "modules":    "Modules & Packages",
}

class handler(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        try:
            length  = int(self.headers.get('Content-Length', 0))
            body    = self.rfile.read(length)
            data    = json.loads(body)

            topic_id      = data.get('topic', 'oops')
            difficulty    = data.get('difficulty', 'medium')
            num_questions = min(int(data.get('num_questions', 5)), 15)
            topic_label   = TOPICS.get(topic_id, 'OOPs & Classes')

            api_key = os.environ.get('GROQ_API_KEY')
            client  = Groq(api_key=api_key)

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

            chat = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
                temperature=0.7,
            )
            raw   = chat.choices[0].message.content.strip()
            match = re.search(r'\[.*\]', raw, re.DOTALL)

            if match:
                questions = json.loads(match.group())
                result = {"success": True, "questions": questions, "topic": topic_label, "difficulty": difficulty}
            else:
                result = {"success": False, "error": "Could not parse AI response"}

        except Exception as e:
            result = {"success": False, "error": str(e)}

        response = json.dumps(result).encode()
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-Length', str(len(response)))
        self.end_headers()
        self.wfile.write(response)
