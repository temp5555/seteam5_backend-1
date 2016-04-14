from gcm import GCM
import database_driver
from twilio.rest import TwilioRestClient


def send_message(from_, to_, message):
    gcm = GCM('AIzaSyDhV40wQvZwBIn1rwEJmIy4njUkaMNLvK4')

    data = {'message': message, 'from_': from_}
    registration_ids = database_driver.get_gcm_token(to_)
    gcm.json_request(registration_ids, data)


def send_sms(myTwilioNumber,myCellPhone,message):
	accountSID = 'AC9ca04bf819393f32f29cc73f007b2deb'
	authToken = 'b791d0d1391c8f24c1a48df1d8755a65'
	twilioCli = TwilioRestClient(accountSID, authToken)
	message = twilioCli.messages.create(body=message, from_=myTwilioNumber, to=myCellPhone)


#remove the comments below to run a test

#msg = "Running test"
#send_sms('+12016902826','+918050642408',msg)
