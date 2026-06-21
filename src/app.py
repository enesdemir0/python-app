from flask import Flask, jsonify
import datetime, socket

app = Flask(__name__)

@app.route('/api/v1/info')
def get_info():
    info = {
        'hostname': socket.gethostname(),
        'timestamp': datetime.datetime.now().isoformat()
    }
    return jsonify(info)

@app.route('/api/v1/health')
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)