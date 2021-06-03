from flask import Flask, render_template, request, redirect
from helper_db import *

app = Flask(__name__)

BASE_URL = ''

@app.route('/')
def index():
    global BASE_URL
    BASE_URL = request.url
    return render_template('index.html', short_url='')

@app.route('/long_url', methods=['POST'])
def long_url():
    global BASE_URL
    if request.method == 'POST':

        url = request.form.get('url')
        url = validate(url)
        short_url = exist(url)

        if short_url == None:
            short_url = generate_short_url()
            insert_url(validate(url), short_url)

        short_url_display = BASE_URL + short_url

        return render_template('index.html', short_url=short_url_display)

@app.route('/<short_url>')
def redirect_to_url(short_url):
    url = get_url(short_url)
    print(url)
    if url != None:
        return redirect(url)
    else:
        return render_template('not_found.html')



if __name__ == '__main__':
    app.run(port=5000, debug=True)