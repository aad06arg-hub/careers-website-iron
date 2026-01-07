from flask import Flask

app = Flask(__name__)

@app.route('/')
def website_1():
  return "<h1>This is website 1 view</h1>"
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

