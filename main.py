from bottle import Bottle, route, run, template
from faker import Faker
import datetime
import json
import paho.mqtt.client as paho

app = Bottle()
fake = Faker(['fr_FR', 'en_US'])


@app.route('/')
def home():
    return template('<b>Dashboard</b>!')

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name="world"):
    return template('<b>Hello {{name}}</b>!', name=name)
    
@app.route('/broker/push')
def broker_push():
    i=0
    Faker.seed(0)
    while i<10:
        # temperature = read_from_imaginary_thermometer()
        data = {'name': fake.name(), "value": fake.pyint(1, 100), 'date': datetime.datetime.now()}
        print("data", data)
        data = json.dumps(data)
        print("data", data)
        (rc, mid) = msg_info = client.publish('encyclopedia/temperature', data, qos=1)
        if msg_info.is_published() == False:
            print('Message is not yet published.')
        # This call will block until the message is published.
        msg_info.wait_for_publish()
        time.sleep(2)
        print("rc", rc, "mid", mid)
        i=i+1
    return template('broker_push {{data}}', data, i)

@app.route('broker/pull')    
def borker_pull():
    data = {}
    
    # client.subscribe('encyclopedia/#', qos=1)
    # client.loop_forever()
    
    return template('broker_pull {{data}}', data)

run(app, host='0.0.0.0', port=8080)
