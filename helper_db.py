import sqlite3
import random
import string

def check_short_url(short_url):
    '''check db if short url exists'''
    db = sqlite3.connect('url.db')
    c = db.cursor()

    c.execute("SELECT short_url FROM URL")
    all_url = c.fetchall()
    db.close()

    if short_url not in all_url:
        return True
    return False

def generate_short_url():
    short_url = ''
    while True:
        for i in range(6):
            while True:
                rand_letter = random.choice(string.ascii_letters)
                if rand_letter not in short_url:
                    short_url += rand_letter
                    break

        if check_short_url(short_url):
            return short_url

def insert_url(long_url, short_url):
    '''insert urls into db'''
    db = sqlite3.connect('url.db')
    c = db.cursor()

    c.execute("INSERT INTO URL (url, short_url) VALUES (:long_url, :short_url)", (long_url, short_url))
    db.commit()
    db.close()

def get_url(short_url):
    db = sqlite3.connect('url.db')
    c = db.cursor()
    c.execute("SELECT url FROM URL WHERE short_url=:short_url", [short_url])
    url = c.fetchone()
    if url != None:
        url = url[0]
    return url

def exist(url):
    db = sqlite3.connect('url.db')
    c = db.cursor()
    c.execute('SELECT short_url FROM URL WHERE url=:url', [url])
    short_url = c.fetchone()
    if short_url == None:
        return None
    else:
        return short_url[0]

def validate(url):
    header = 'https://www'
    split_url = url.split('.')
    head = split_url[0]
    if head != header:
        if head in header:
            split_url[0] = header
        else:
            split_url.insert(0, header)
        url = '.'.join(split_url)
    return url