from flask import Flask 
from flask_restful import Resource , Api,reqparse
import json ,time
import datetime

app = Flask (__name__)
api = Api(app) 

parser = reqparse.RequestParser()
parser.add_argument('day')
parser.add_argument('month')
parser.add_argument('year')

def cal_date(birthdate):
    today = datetime.datetime.now()
    if today.month < birthdate.month or today.month == birthdate.month and today.day < birthdate.day:
        return today.year - birthdate.year - 1
    else:
        return today.year - birthdate.year

class Hello(Resource):
	def get(self): 
		args = parser.parse_args()
		Day = args['day']
		Month = args['month']
		Year = args['year']
		birthdate = datetime.date(int(Year), int(Month), int(Day))
		caldate=cal_date(birthdate)
		return {"Born":str(birthdate),"Age": str(caldate)}

api.add_resource(Hello,'/timestamp')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5500)
