from flask import Flask

app = Flask(__name__)

def suma(a,b):
  return a+b

@app.route("/")
def hello():
    rest = suma(3,3)
    return "Hello friend %s" % (rest)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)
