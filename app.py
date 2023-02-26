from flask import Flask, render_template

app = Flask(__name__)
JOBS = [
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Dhaka, Bangladesh',
    'salary':'$90,000'
  },
  {
    'id':2,
    'title':'Data scientist',
    'location':'Dhaka, Bangladesh',
    'salary':'$100,000'
  },
  {
    'id':3,
    'title':'Front-end developer',
    'location':'Chittagong, Bangladesh',
    'salary':'$50,000'
  },
  {
    'id':4,
    'title':'Back-end Engineer',
    'location':'Dhaka, Bangladesh',
    'salary':'$120,000'
  }
  
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs = JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  
