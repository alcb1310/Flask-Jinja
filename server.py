from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)

    copy_year = datetime.now().year

    return render_template('index.html', num=random_number, copy_year=copy_year)


@app.route("/guess/<string:name>")
def guess_route(name: str):
    res = requests.get(f'https://api.genderize.io?name={name.lower()}')
    res.raise_for_status()
    gender = res.json()['gender']

    res = requests.get(f'https://api.agify.io?name={name.lower()}')
    res.raise_for_status()
    age = res.json()['age']

    return render_template('guess.html', name=name.title(), gender=gender, age=age)


@app.route("/blog/<int:num>")
def get_blog(num: int):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    res = requests.get(blog_url)
    res.raise_for_status()
    all_posts = res.json()

    print(num)

    return render_template('blog.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
