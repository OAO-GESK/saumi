from flask import Flask, render_template, url_for, request
import cx_Oracle as ora

cpar={
	'usr': 'sm',
	'pas': 'smpwd',
	'enc': 'UTF-8',
}
cpar['dsn'] = ora.makedsn('localhost', '1521')

app = Flask('SaumiAddon', static_folder='assets')

@app.route('/')
def index():
	return "<h1>Hello bro!</h1>"

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
		cn = ora.connect(user=cpar['usr'], password=cpar['pas'], dsn=cpar['dsn'])
		cur = cn.cursor()
		try:
			cur.execute(q)
		except Exception as e:
			return str(e)
		s = '<table>'
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
