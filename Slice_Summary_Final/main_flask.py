from flask import Flask, request, jsonify
from main import main
import traceback

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask 服务已启动！请访问 /process 接口提交数据。", 200

@app.route('/favicon.ico')
def favicon():
    return "", 204

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.get_json()
        required_fields = ['openai_or_dify', 'mode', 'txt', 'window_size', 'overlap_size', 'url_input']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        result = main(
            openai_or_dify=data['openai_or_dify'],
            mode=data['mode'],
            txt=data['txt'],
            window_size=data['window_size'],
            overlap_size=data['overlap_size'],
            url_input=data['url_input'],
            prompt_single=data.get('prompt_single'),
            prompt_two_or_more=data.get('prompt_two_or_more'),
            api_key_input=data.get('api_key_input'),
            model_input=data.get('model_input'),
            api_key_input_1=data.get('api_key_input_1'),
            api_key_input_2=data.get('api_key_input_2')
        )
        return jsonify({
            "msg": "success",
            "code": 200,
            "data": result  # 你的处理结果
        })

    except Exception as e:
        traceback.print_exc()  # 打印异常堆栈信息
        return jsonify({
            "msg": str(e),
            "code": 500
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)