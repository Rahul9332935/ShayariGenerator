from flask import Flask, render_template, request, jsonify
import openaiData
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    
    return render_template('index.html')
@app.route("/GeneratShayari/val", methods=["POST"])
def generatS():
  data= request.form
  d=openaiData.generateShayari(data['value'])
  print(d)
  return d

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)