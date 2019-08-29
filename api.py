from flask import Flask
from flask import request, jsonify

app = Flask(__name__)
app.config['DEBUG']=True


phones = [
    {'id': 0,
     'model': 'Samsung',
     'color': 'Black',
     'OS': 'Android',
     'size': '5"'},

    {'id': 1,
     'model': 'Huawei',
     'color': 'Gold',
     'OS': 'Android',
     'size': '5"'},

    {'id': 2,
     'model': 'Tecno',
     'color': 'Blue',
     'OS': 'Android',
     'size': '6"4'},

    {'id': 3,
     'model': 'Iphone 6',
     'color': 'White',
     'OS': 'IOS',
     'size': '6"'},    
]


@app.route('/', methods=['GET'])
def hello():
    return "<h1>Phones for display</h1><p>Welcome, start windowshopping now! You....</p>"

@app.route('/api/store/phones/all', methods=['GET'])
def phones_list():
	return jsonify(phones)

@app.route('/api/store/phones', methods=['GET'])
def api_id():
	if 'id' in request.args:
		id=int (request.args['id'])
	else:
		return "Error: No specified id"

	results=[]

	for phone in phones:
		if phone['id']==id:
			results.append(phone)
	return jsonify(results)


app.run()


