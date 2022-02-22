from flask import Flask,jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'name': u'father',
        'contact': u'9462526266', 
        'done': False
    },
    {
        'id': 2,
        'name': u'mother',
        'contact': u'9086745476', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-contact", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json.get('contact', ""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-contact")
def get_contact():
    return jsonify({
        "data" : contacts
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)