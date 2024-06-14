from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index_1():
    content = None

    if request.method == 'POST':
        author = request.form['author']
        content = get_content(author)
    return render_template("index_1.html", content=content)



def get_content(autor):
    url = f"https://api.quotable.io/random"
    response = requests.get(url)
    return response.json()






if __name__ == '__main__':
    app.run(debug=True)