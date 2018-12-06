from flask import Flask, render_template, url_for, request
import cx_Oracle as ora
from params import cpar

app = Flask('SaumiAddon', static_folder='assets')

@app.route('/')
def index():
	dsn = ora.makedsn(cpar['host'], '1521')
	cn = ora.connect(user=cpar['usr'], password=cpar['pas'], encoding=cpar['enc'], dsn=dsn)
	cur = cn.cursor()
	objects = grounds = buildings = None
	cur.execute('select count(*) from objects')
	for row in cur: objects = row[0]
	cur.execute('select count(*) from grounds')
	for row in cur: grounds = row[0]
	cur.execute('select count(*) from buildings')
	for row in cur: buildings = row[0]
	return render_template('startpage.html', totalobjects=objects, totalgrounds=grounds, totalbuildings=buildings)


@app.route('/find', methods=['POST'])
def find():
	return 'Errow'


@app.route('/admin/<int:id>')
def admin(id=0):
	if id != 31628:
		return url_for('static', filename='js/engine.js')
	return render_template('admin.html')


@app.route('/admin/dbquery', methods=['POST'])
def dbquery():
	if request.method == 'POST':
		q = request.form['query']
		if 'update' in q:
			return '<b>UPDATE</b> query not allowed here!'
		dsn = ora.makedsn(cpar['host'], '1521')
		cn = ora.connect(user=cpar['usr'], password=cpar['pas'], encoding=cpar['enc'], dsn=dsn)
		cur = cn.cursor()
		try:
			cur.execute(q)
		except Exception as e:
			return str(e)
		s = '<table class="table">'
		for row in cur:
			s += '<tr>'
			for el in row:
				s += '<td>' + str(el) + '</td>'
			s += '</tr>'
		s += '</table>'
		cur.close()
		cn.close()
		return s

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')
