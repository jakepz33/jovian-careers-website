from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'San Diego, California',
  'salary': '100,000'
}, {
  'id': 2,
  'title': 'Backend engineer',
  'location': 'Remote',
  'salary': '120,000'
}, {
  'id': 3,
  'title': 'Systems Engineer',
  'location': 'San Diego, California',
  'salary': '110,000'
}, {
  'id': 4,
  'title': 'Cloud Engineer',
  'location': 'San Diego, California',
  'salary': '140,000'
}]


# when the URL "/" is accessed, show Hello World
@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name="Jovian")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


print(__name__)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)  #provide a host
#testing more commites
