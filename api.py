import os

from flask import Flask, request, jsonify

from aws_handler import upload_file
from visual_regression import VisualRegression

app = Flask(__name__)


@app.route('/', methods=['POST'])
def test_regression():
    if 'baseline' not in request.files or 'test' not in request.files:
        resp = jsonify({'message' : "'baseline' or 'test' files were not found"}) 
        resp.status_code = 400
        return resp

    baseline = request.files['baseline']
    test = request.files['test']
    
    regression_test = VisualRegression(baseline, test)
    has_regression, result_file = regression_test.analyze()

    if not has_regression:
        resp = jsonify({'message': 'Visual regression not found'})
        resp.status_code = 200
        return resp
    
    file_url = upload_file(result_file)
    resp = jsonify({
        'message': 'Visual regression found',
        'file_url': file_url
    })
    resp.status_code = 200
    return resp


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

