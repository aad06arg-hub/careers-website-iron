from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 45178,
    'title': 'Python Developer',
    'location': 'San Francisco, CA',
    'Salary': '$150,000'
  },
  {
    'id': 78341,
    'title': 'UI Designer',
    'location': 'Cupertino, CA',
    'Salary': '$130,000'
  },
  {
  'id': 65937,
  'title': 'Database Administrator',
  'location': 'Manhattan, NY',
  'Salary': '$110,000'
  }
]

@app.route('/')
def website_1():
  return render_template('home.html', jobs=JOBS, )
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

