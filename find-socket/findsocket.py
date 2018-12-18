from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from confparser import *
from flask_script import Manager


class SocketForm(FlaskForm):
    '''
    form for ethernet socket page
    '''
    # field for enter socket number
    ethsocket = StringField('Enter socket number:', validators=[Required()])
    # submit button
    searchbutton = SubmitField('Search')


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'Set_your-Secret3Key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/socket', methods=['GET', 'POST'])
def socket():
    __CONF_DIR = "/configs/dir"
    __HW_EXCLUSIONS = ["<router1>", "<router2>"]
    ethsocket = None
    form = SocketForm()
    if form.validate_on_submit():
        last_config_list = lastConfig(__CONF_DIR, __HW_EXCLUSIONS)
        ethsocket = findEthPort(form.ethsocket.data, last_config_list)
    return render_template('socket.html', ethsocket=ethsocket, form=form)


manager = Manager(app)

if __name__ == '__main__':
    manager.run()
