from flask import Flask, render_template
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
    return render_template ('home.html', jobs=JOBS)
if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)
  