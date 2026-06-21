from flask import Flask, render_template
import json

app = Flask(__name__)

visit_count = 0

@app.route("/")
def home():
    global visit_count
    visit_count += 1

    with open("employees.json", "r") as f:
        employees = json.load(f)

    return render_template(
        "index.html",
        employees=employees,
        visit_count=visit_count
    )

if __name__ == "__main__":
    app.run(debug=True)
