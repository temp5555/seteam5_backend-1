import os
import pymongo

URL = os.environ.get("OPENSHIFT_MONGODB_DB_URL")
if URL:
    client = pymongo.MongoClient(URL)
else:
    client = pymongo.MongoClient("localhost", 27017)


def post_userinfo(userinfo):
    db = client.backend
    info = {}
    for k, v in userinfo.items():
        info[k] = v
    return db.userinfo.insert_one(info)


def get_userinfo(phonenumber):
    db = client.backend
    row = db.userinfo.find_one({"phonenumber": phonenumber})
    if not row:
        return {}
    info = {}
    for k, v in row.items():
        info[k] = v
    if '_id' in info:
        info.pop('_id', None)
    return info


def add_route(phonenumber, route):
    db = client.backend
    info = {}
    info[phonenumber] = route
    return db.routeinfo.insert_one(info)


def get_students_info(query):
    db = client.backend
    rows = db.userinfo.find(query)
    return rows


def update_student_info(updated_info):
    db = client.backend
    db.userinfo.update({'phonenumber': updated_info['phonenumber']},
                       {'$set': {'status': updated_info['status']}},
                       True)


def get_unassigned_students():
    db = client.backend
    rows = db.userinfo.find({"route": {"$exists": False}})
    return rows
