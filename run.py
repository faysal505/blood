from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('test.html')

@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        blood = request.form['blood']
        report = request.form['report']
        return render_template('blood.html', name=name, age=age, blood=blood, report=report)
    return render_template('test.html')

if __name__ == '__main__':
    app.run()
