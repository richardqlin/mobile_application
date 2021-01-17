from flask import *

from flask_bootstrap import Bootstrap

from database import Database
from datetime import datetime

from pytz import timezone,utc

app = Flask('mobile_app')

Bootstrap(app)




@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/')
def index():
    entries=Database.get_records()
    return render_template('index.html', entries=entries)


@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        utc = datetime.now(timezone('UTC'))
        p = utc.astimezone(timezone('US/Pacific'))
        data = {
            'title': request.form['title'],
            'post': request.form['post'],
            'time': p.strftime('%I:%M:%S %p'),
            'date':p.strftime('%Y-%m-%d' )
        }
        Database.insert_record(data)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete')
def delete_entries():
    print('delete')
    Database.delete_all_records()
    return redirect('/')

@app.route('/entries')
def entry():
    entries = Database.get_records()
    for entry in entries:
        entry['_id'] = str(entry['_id'])
    return json.dumps(entries)

@app.route('/remove/<id>')
def delete_id(id):
    Database.delete(id)
    return redirect('/')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0',debug=True)
