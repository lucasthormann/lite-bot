import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, make_response
from embed import embed
from query import query
from delete import delete_persisted_db
from get_vector_db import get_vector_db

load_dotenv()
TEMP_FOLDER = os.getenv('TEMP_FOLDER', './_temp')
os.makedirs(TEMP_FOLDER, exist_ok=True)

app = Flask(__name__)

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response  
    
@app.route('/delete', methods=['DELETE'])
def route_delete():
    try:
        delete_persisted_db()
        return {"message": "Database has been deleted."}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))  

@app.route('/embed', methods=['POST'])
def route_embed():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    embedded = embed(file)
    return jsonify({"message": "File embedded successfully"}) if embedded else jsonify({"error": "Embedding failed"}), 400

@app.route('/query', methods=['POST', 'OPTIONS'])
def route_query():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    elif request.method == "POST": # The actual request following the preflight
        data = request.get_json()
        response = query(data.get('query'))
        return _corsify_actual_response(jsonify(response))
    else:
        raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))
        
def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
    

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
