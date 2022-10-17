from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)

    copy_year = datetime.now().year

    return render_template('index.html', num=random_number, copy_year=copy_year)


if __name__ == "__main__":
    app.run(debug=True)
