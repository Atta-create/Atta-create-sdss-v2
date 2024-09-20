from flask import Flask, render_template, jsonify 
app = Flask(__name__)
JOBS = [
        {
      'id':1,
      'title': 'Team Lead',
      'location': 'SDSS Lab, BUITEMS Quetta',
      'salary': 'Rs. 1,000,00'
       },
       {
      'id':2,
      'title': 'Research Associate',
      'location': 'SDSS Lab, BUITEMS Quetta',
      'salary': 'Rs. 70,000'
       },
       {
      'id':3,
      'title': 'Research Assistant',
      'location': 'SDSS Lab, BUITEMS Quetta',
      'salary': 'Rs. 50,000'
       },
       {
      'id':4,
      'title': 'Web Developer',
      'location': 'SDSS Lab, BUITEMS Quetta',
      'salary': 'Rs. 50,000'
       }
    ]
 
@app.route("/")
def hello_SDSS():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
   return jsonify(JOBS)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/get_involved')
def get_involved():
    return render_template('get_involved.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True)
  