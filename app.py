from flask import Flask, abort, make_response, request, render_template

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sre', methods=['POST'])
def sre():
    content = request.get_json()

    if content is None:
        abort(404)
    res = make_response(content)
    return res

if __name__ == '__main__':
    app.run()