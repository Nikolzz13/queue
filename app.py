from flask import Flask, render_template

app = Flask (__name__)

@app.route ('/')
def index():
    listmap = [{'Name':"Проф. орентация","link":123},{'Name':"Забрать документы","link":123},{'Name':"Забрать документы","link":123},{'Name':"Донести Документ","link":123}]
    return render_template("index.html",listed = listmap)
@app.route('/monitor')
def monitor():
    return render_template("monitor.html")
@app.route('/meneger')
def meneger():
    return render_template("meneger.html")
@app.route('/operator')
def operator():
    return render_template("operator.html")
@app.route('/admin')
def admin():
    return render_template("admin.html")
if __name__ == '__main__':
    app.run()