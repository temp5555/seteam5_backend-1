from flask import Flask, request, jsonify

import database_driver

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world!', 200


@app.route('/userinfo/', methods=['POST'])
def post_userinfo():
    if 'phonenumber' not in request.form:
        return 'Missing phonenumber', 400
    current_info = database_driver.get_userinfo(request.form['phonenumber'])
    if current_info:
        return 'Data exist! make put request to entirely replace', 409
    result = database_driver.post_userinfo(request.form)
    if not result:
        return 'Illegal request', 400
    else:
        return 'Success', 201


@app.route('/userinfo/<phonenumber>', methods=['GET'])
def get_userinfo(phonenumber):
    info = database_driver.get_userinfo(phonenumber)
    if not phonenumber or not info:
        return 'Not found', 404
    return jsonify(info)


if __name__ == '__main__':
    app.run(debug=True)
