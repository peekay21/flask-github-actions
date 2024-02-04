from flask import Flask

app = Flask(__name__)
app.config['TESTING'] = True

@app.route("/")
def hello_world():
  return "<p>Hello, Pradip Kumar Murmu!</p>"

if __name__ =="__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
