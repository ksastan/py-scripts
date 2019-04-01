from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_script import Manager
import models


class LicensesForm(FlaskForm):
    '''
    form shows all licenses
    '''
    software_name = StringField('Enter software name:', validators=[Required()])
    # submit button
    searchbutton = SubmitField('Search')


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'Set_your-Secret3Key'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showlall', methods=['GET', 'POST'])
def showall():
    all_licenses = models.get_all_licenses()
    return render_template('showall.html', all_licenses=all_licenses)

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
