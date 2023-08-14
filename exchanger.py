import requests
import json
from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    response = requests.get(url='https://v6.exchangerate-api.com/v6/40bc0bdae61341100ad9584e/latest/USD')
    currencies = response.json().get('conversion_rates')

    if request.method == 'GET':
        with open('response.json', 'w') as file:
            json.dump(response.json(), file, indent=4)
        return render_template(template_name_or_list='index.html', currencies=currencies)
    elif request.method == 'POST':
        amount = request.form['amount']
        give_curr = request.form['give_curr']
        take_curr = request.form['take_curr']
        converted_amount = round((currencies[take_curr] / currencies[give_curr]) * float(amount), 2)
        return render_template(template_name_or_list='index.html',
                               currencies=currencies,
                               converted_amount=converted_amount)


@app.route('/about')
def about():
    return render_template(template_name_or_list='about.html')


if __name__ == '__main__':
    app.run(debug=True)
