from flask import Flask, render_template
import os

# Imposta il percorso assoluto della cartella templates
app = Flask(__name__, template_folder=os.path.join(os.getcwd(), "templates"))

# Lista di link personalizzati
links = [
    {"name": "Instagram", "url": "https://www.instagram.com/peppary_?igsh=MWF1OXo0dnN6NW81cw=="},
    {"name": "TikTok", "url": "https://www.tiktok.com/@ary.pink0?_t=ZN-8uhgVNhrG3q&_r=1"}
]

@app.route("/")
def home():
    return render_template("index.html", links=links)

if __name__ == "__main__":
    print(f"Server in esecuzione su: http://127.0.0.1:5000")
    app.run(debug=True, host="0.0.0.0", port=5000)
