from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'San Francisco, CA',
        'salary': '$120,000 - $180,000',
        'description': 'Join our engineering team to build amazing products.'
    },
    {
        'id': 2,
        'title': 'Product Manager',
        'location': 'New York, NY',
        'salary': '$130,000 - $170,000',
        'description': 'Lead product strategy and work with cross-functional teams.'
    },
    {
        'id': 3,
        'title': 'Data Scientist',
        'location': 'Remote',
        'salary': '$110,000 - $160,000',
        'description': 'Analyze data and build machine learning models.'
    },
    {
        'id': 4,
        'title': 'UX Designer',
        'location': 'Austin, TX',
        'salary': '$90,000 - $130,000',
        'description': 'Create beautiful and intuitive user experiences.'
    }
]


@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS)


@app.route('/job/<int:job_id>')
def job_detail(job_id):
    job = next((j for j in JOBS if j['id'] == job_id), None)
    return render_template('job.html', job=job)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
