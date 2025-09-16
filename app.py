from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "سلام — ربات تستی پایتون بالا آمد ✅"

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/message", methods=["POST"])
def message():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "")
    reply = f"دریافت شد: {text}"
    return jsonify(reply=reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
