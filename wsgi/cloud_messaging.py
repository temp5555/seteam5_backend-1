from gcm import GCM
import database_driver


def send_message(from_, to_, message):
    gcm = GCM('AIzaSyDhV40wQvZwBIn1rwEJmIy4njUkaMNLvK4')

    data = {'message': message, 'from_': from_}
    registration_ids = database_driver.get_gcm_token(to_)
    gcm.json_request(registration_ids, data)
