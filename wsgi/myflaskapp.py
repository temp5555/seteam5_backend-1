from flask import Flask, request, jsonify, render_template

import database_driver

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world!', 201


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


@app.route('/admin/login')
def admin_login():
    return render_template("admin_login.html")


@app.route('/admin_student_status.html', methods=['GET'])
def admin_student_status():
    pending = database_driver.get_students_info({"status": {"$exists": False}})
    approoved = database_driver.get_students_info({"status": "aproove"})
    declined = database_driver.get_students_info({"status": "decline"})
    return render_template('admin_student_status.html', pending=pending,
                           approoved=approoved, declined=declined)

@app.route('/map.html')
def map():
    return render_template("map.html")

@app.route('/admin_student_status.html', methods=['POST'])
def admin_student_status_update():
    update = {"phonenumber": request.form['phonenumber'],
              "status": request.form['status'],
              }
    database_driver.update_student_info(update)
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)
