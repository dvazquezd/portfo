from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def works(page_name):
    return render_template(page_name)


def write_inf(data):
    try:
        with open('database.csv', mode='a') as database:
            email = data['email']
            subject = data['subject']
            message = data['message']
            csv_writer = csv.writer(database, delimiter=',')
            csv_writer.writerow([email, subject, message])
    except TypeError as err:
        print(f'Error: {err}')


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    print(request.method)
    if request.method == 'POST':
        try:
            email = request.values.get('email')
            subject = request.values.get('subject')
            message = request.values.get('message')
            data = {'email': email, 'subject': subject, 'message': message}
            print(data)
            write_inf(data)
            return redirect("/submit.html")
        except:
            print('Something went wrong. Try again')
