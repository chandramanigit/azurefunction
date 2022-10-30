from flask import Flask , request , jsonify , render_template 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello/<name>", methods=['GET'])
def hello(name: str):
    return f"hello {name}"

@app.route("/alert", methods=['POST'])
def alerts():
    global data
    data = request.json
    return jsonify(data)
    print(data)
  
@app.route("/alert_display",methods=["GET"])
def display():
    return jsonify(data)

if __name__ == "__main__":
    app.run()
