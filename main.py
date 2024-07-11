from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/novel', methods=['GET'])
def get_novel():
    try:
        with open('novel.txt', 'r', encoding='utf-8') as file:
            novel_content = file.read()
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404

    page = request.args.get('page', default=1, type=int)
    per_page = 200  # 每页显示的字符数
    start = (page - 1) * per_page
    end = start + per_page

    if start >= len(novel_content):
        return jsonify({'error': 'Page out of range'}), 404
    
    content = novel_content[start:end]

    return content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
