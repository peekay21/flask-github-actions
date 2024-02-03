from flask improt Flask

app = Flaks(__name__)
app.config['TESTING'] = True

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

if __name__ =="__main__:
  app.run(debug=True)
