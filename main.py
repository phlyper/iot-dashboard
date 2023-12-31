import bottle
from bottle import Bottle, route, get, post, request, run, template, jinja2_view
from bottle import Jinja2Template, url, static_file
import functools
# from faker import Faker
import config.bootstrap

from datetime import date, datetime
import json
import paho.mqtt.client as paho

Jinja2Template.defaults = {
    'url': url,
    'site_name': 'My blog',
}

view = functools.partial(jinja2_view, template_lookup=["templates"])

app = Bottle()
# fake = Faker(['fr_FR', 'en_US'])

@app.route('/')
@view('index.html')
def home():
    rows = {}

    # cursor object c
    mycursor = config.bootstrap.dbc.cursor()

    # executing the create database statement
    mycursor.execute("SELECT * FROM data_object WHERE object IS NOT NULL AND detected_at IS NOT NULL ORDER BY detected_at DESC LIMIT 0, 100")

    rows['latest'] = mycursor.fetchall()
    # rows['latest'] = []
    # for x in mycursor.fetchall():
    #     rows['latest'].append(x)

    mycursor.close()

    # cursor object c
    mycursor = config.bootstrap.dbc.cursor()

    # executing the create database statement
    mycursor.execute("SELECT DISTINCT(`object`) FROM data_object WHERE object IS NOT NULL")

    rows['list_objects'] = mycursor.fetchall()
    # rows['objects'] = []
    # for x in mycursor.fetchall():
    #     rows['objects'].append(x)

    mycursor.close()

    # cursor object c
    mycursor = config.bootstrap.dbc.cursor()

    # executing the create database statement
    mycursor.execute("SELECT object, count(id) as count_object, detected_at FROM data_object WHERE object IS NOT NULL GROUP BY object ORDER BY detected_at DESC")

    rows['objects'] = mycursor.fetchall()
    # rows['objects'] = []
    # for x in mycursor.fetchall():
    #     rows['objects'].append(x)

    mycursor.close()

    # cursor object c
    mycursor = config.bootstrap.dbc.cursor()

    # executing the create database statement
    mycursor.execute("SELECT date(detected_at) as `detected_date`, COUNT(`id`) as `count_object` FROM data_object WHERE object IS NOT NULL GROUP BY date(detected_at) ORDER BY detected_at DESC")

    rows['list_byday'] = mycursor.fetchall()
    # rows['objects'] = []
    # for x in mycursor.fetchall():
    #     rows['objects'].append(x)

    mycursor.close()

    print(rows)

    return {'title': '<b>Dashboard</b>!', 'rows': rows }

@app.route('/dashboard')
@view('dashboard.html')
def dashboard():
    rows = {}
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        rows['type'] = 'This is an AJAX request'

        # cursor object c
        mycursor = config.bootstrap.dbc.cursor()

        # executing the create database statement
        mycursor.execute("SELECT object, accuracy, count(id) as count_object, detected_at, read_at, id FROM data_object WHERE object IS NOT NULL AND read_at IS NULL GROUP BY object ORDER BY detected_at ASC;")

        rows['objects'] = mycursor.fetchall()

        print(rows)

        for index in range(len(rows['objects'])):
            row = list(rows['objects'][index])
            print('row v1', row)

            for key in range(len(row)):
                if isinstance(row[key], (datetime, date)):
                    row[key] = row[key].isoformat()

            rows['objects'][index] = tuple(row)
            print('row v2', rows['objects'][index])

        mycursor.close()

        x = datetime.now()

        # cursor object c
        mycursor = config.bootstrap.dbc.cursor()

        # executing the create database statement
        mycursor.execute("UPDATE `data_object` SET read_at= %s WHERE read_at IS NULL LIMIT 1;", (x.strftime("%Y-%m-%d %H:%M:%S"),))

        mycursor.close()

        # rows['objects'] = {"i": "b"}

        return json.dumps(rows)

    return {'title': '<b>Dashboard</b>!'}

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
        data = {'name': fake.name(), "value": fake.pyint(1, 100), 'date': datetime.now()}
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

if __name__ == "__main__":
    bottle.debug(True)

    @app.route('/assets/<filepath:path>')
    def server_static(filepath):
        print(filepath)
        return bottle.static_file(filepath, root='./assets/')
        # yield

    run(app, host='0.0.0.0', port=86, reloader=True, debug=True)
