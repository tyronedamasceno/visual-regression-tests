from flask import Flask, request, jsonify

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
    
    resp = jsonify({
        'message': 'Visual regression found',
        'file_path': result_file
    })
    resp.status_code = 200
    return resp


if __name__ == "__main__":
    app.run()

