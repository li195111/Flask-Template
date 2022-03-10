from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app,
     resources={r'/*':{'origins':'*'}},
     origins=["*"])

@app.route('/')
async def index():
    q = request.args
    return {'q':q}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True, load_dotenv=True)