from flask import Flask, send_file

app = Flask(__name__)

@app.route('/novel', methods=['GET'])
def get_novel():
    return send_file('novel.txt', as_attachment=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
