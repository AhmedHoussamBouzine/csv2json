from flask import Flask, request, jsonify
import pandas as pd
import os
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'

for folder in [UPLOAD_FOLDER, OUTPUT_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER


@app.route('/upload', methods=['POST'])
def upload_file():
 
    try:
        
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        if file and file.filename.endswith('.csv'):
            # Save the uploaded CSV file
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            # Convert CSV to JSON
            df = pd.read_csv(filepath)
            json_data = df.to_json(orient='records')
            # Save JSON to a file
            json_filename = file.filename.rsplit('.', 1)[0] + '.json'
            json_filepath = os.path.join(app.config['OUTPUT_FOLDER'], json_filename)
            with open(json_filepath, 'w') as json_file:
                json_file.write(json_data)
            return jsonify(json_data=json_data, message="File saved successfully", file_path=json_filepath)
        else:
            return jsonify({"error": "Invalid file format. Please upload a CSV file."}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

if __name__ == '__main__':
    app.run(debug=True)
