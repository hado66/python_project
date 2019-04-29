from flask import Flask,render_template,Markup

app=Flask(__name__)
app.debug=True

def func(agrs):
    return agrs+"this is fun"

def func1(args):
    return Markup('<input type="text" value="%s">'%(args))


@app.route('/hello',endpoint='n')
def hello():
    return render_template("s10index.html",xx='dd')

if __name__ == '__main__':
    app.run()