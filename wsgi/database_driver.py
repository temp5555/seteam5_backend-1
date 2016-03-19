import os
import pymongo

URL = os.environ.get("OPENSHIFT_MONGODB_DB_URL")
if URL:
    client = pymongo.MongoClient(URL)
else:
    client = pymongo.MongoClient("localhost", 27017)
client.drop_database("backend")

def post_userinfo(userinfo):
    db = client.backend
    info = {}
    for k, v in userinfo.items():
        info[k] = v
    return db.userinfo.insert_one(info)
#put location as a val

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


def get_students_info(**kwargs):
    db = client.backend
    rows = db.userinfo.find(**kwargs)
    return rows
