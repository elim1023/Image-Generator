import os
from flask import Flask, render_template, request, redirect, url_for, session
from application.main import generateImg

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/generate", methods=["POST", "GET"])
def generate():
    if request.method == "POST":
        prompt = request.form.get("prompt")
        size = request.form.get("size")

        if prompt and size:
            session["prompt"] = prompt
            session["size"] = size
            return redirect(url_for("success"))

    return redirect(url_for("home"))

@app.route("/success")
def success():
    if "prompt" not in session or "size" not in session:
        return redirect(url_for("home"))

    prompt = session["prompt"]
    size = session["size"]

    try:
        url = generateImg(prompt, size)
    except Exception as e:
        return f"Image generation failed: {str(e)}", 500

    session.pop("prompt", None)
    session.pop("size", None)

    return render_template("index.html", imgUrl=url)

if __name__ == "__main__":
    app.run()
