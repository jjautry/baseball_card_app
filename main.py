from flask import Flask, request, render_template
from csv_converter import baseball_data_dict
from user import add_new_card, search_dict4card

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
