from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def bmi():
    weight=""
    height=""
    bmi=''
    if request.method == 'POST' and 'userweight' and 'userheight' in request.form:
        weight=request.form.get('userweight')
        height=request.form.get('userheight')
        height=(int(height)/100)
        height=(float(height)**2)
        bmi=round((int(weight)/float(height)), 1)
    return render_template('index.html', bmi=bmi)

app.run()