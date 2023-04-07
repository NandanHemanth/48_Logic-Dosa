from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/runastar', methods=['POST'])
def run_astar():
    try:
        result = subprocess.run(['py', 'D:\dotslash\48_Logic-Dosa\flutter_application\lib\astar.py'], capture_output=True)
        message = result.stdout.decode('utf-8')
        return jsonify({'success': True, 'message': message})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
