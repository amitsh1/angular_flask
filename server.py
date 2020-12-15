import os
from flask import Flask, render_template,jsonify
app = Flask(__name__,template_folder="dist/myapp2",static_url_path="", static_folder="dist/myapp2")


@app.route("/")
def index():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000), debug=True)