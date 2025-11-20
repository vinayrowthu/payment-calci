from flask import Flask, request, jsonify, send_from_directory
app = Flask(__name__)

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.json
    expr = data.get('expression', '')
    try:
        safe_expr = ''.join([c for c in expr if c in '0123456789+-*/(). '])
        result = eval(safe_expr, {"__builtins__": None}, {})
        return jsonify({'result': result})
    except Exception:
        return jsonify({'error': 'Invalid Expression'}), 400

@app.route('/', methods=['GET'])
def home():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
