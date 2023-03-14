"""Flask application with embedded chatbot and analytics"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired
import static.plot as plot
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'bdqVBWEsRebA4d@GiXm7'


class NameForm(FlaskForm):

    name = StringField('What is your name?', validators=[DataRequired()])

    submit = SubmitField('Submit')



class Chatbot(FlaskForm):
    response = StringField('How are you feeling today?',
                           validators=[DataRequired()])
    submit = SubmitField('Submit')

class Questions(FlaskForm):

    q1 = StringField('How old are you?', validators=[DataRequired()])
    q2 = StringField('What\'s your weight?', validators=[DataRequired()])
    q3 = StringField('How tall are you?', validators=[DataRequired()])

    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', e=e), 404


name = None
@app.route('/', methods=['GET', 'POST'])
def index():
    global name
    form = NameForm()
    form2 = Questions()
    #name = None
    instr = "Please answer the questions"
    if form.validate_on_submit():
        name = form.name.data
        return render_template('questions.html', form=form2, name=name, instr=instr)
    if form2.validate_on_submit():
        age = float(form2.q1.data)
        weight = float(form2.q2.data)
        height = float(form2.q3.data)
        return render_template('plot.html', plot_url = plot.draw(name,age,weight,height))
    
    return render_template('index.html', form=form, name=name, instr=instr)


@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    form = Chatbot()
    response = None
    if form.validate_on_submit():
        response = form.response.data
    return render_template('chatbot.html', form=form, response=response)


if __name__ == '__main__':
    app.run(port=8000)
