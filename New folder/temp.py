from pandas import Series
from pandas import DataFrame
from pandas import TimeGrouper
from matplotlib import pyplot
import os.path
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# App config.
DEBUG = True
app = Flask(__name__, static_url_path='/static')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    print(name)

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    print (form.errors)
    if request.method == 'POST':
        name=request.form['name']

        series = Series.from_csv('dataset.csv')
        #print(name,"kaam ki jagah")
        nb=name
        groups = series[name].groupby(TimeGrouper('A'))
        years = DataFrame()
        pyplot.figure()
        i = 1
        n_groups = len(groups)
        for name, group in groups:
            pyplot.subplot((n_groups*100) + 10 + i)
            i += 1
            pyplot.plot(group)
            pyplot.savefig('E:/minor/4-FlaskForms/static/pj.jpg')


        #print (name, " in hello")
    
        
        if form.validate():
            
            
            # Save the comment here.
            flash('this is the graph of the rainfall for the year '+nb )

            
        else:
            flash('Error: Enter some value ')
 
    return render_template('hello.html', form=form)

@app.route("/pred")
def predict():
    return render_template('predict.html')

@app.route("/gif")
def gif():
    return render_template('gif.html')


@app.route('/2016')
def model():
    print("in 2016")
    return render_template('2016.html')

 
if __name__ == "__main__":
    app.run()


