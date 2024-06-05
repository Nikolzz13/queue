from flask import Flask, render_template

app = Flask (__name__)

@app.route ('/')
def user(username):
    listmap = [{'Name':"Проф. орентация","link":123},{'Name':"Забрать документы","link":123},{'Name':"Забрать документы","link":123},{'Name':"Донести Документ","link":123}]
    return render_template("index.html",listed = listmap)

if __name__ == '__main__':
    app.run()