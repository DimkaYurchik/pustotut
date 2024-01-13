from flask import Flask
from threading import Thread


app = Flask(__name__)

@app.route('/')
def home():
  return "Hello world"

def run():
  app.run()

def keep_alive():
  t = Thread(target=run)
  t.start()