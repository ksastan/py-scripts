from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import Required, Optional
from flask_script import Manager
import models

class SearchLicenseForm(FlaskForm):
    '''
    search licenses
    '''
    software_name = StringField('Enter software name:')
    end_date = DateField('Expiration date less:', format="%Y-%m-%d", validators=[Optional()])
    searchbutton = SubmitField('Search')

class AddLicenseForm(FlaskForm):
    '''
    add license
    '''
    software_name = StringField('Software name:', validators=[Required()])
    key = StringField('License key:')
    folder = StringField('Folder:')
    version = StringField('Version:')
    start_date = DateField('Start date:', validators=[Required()], format="%Y-%m-%d")
    end_date = DateField('Expiration date:', format="%Y-%m-%d", validators=[Optional()])
    user = StringField('Owner username:', validators=[Required()])
    comment = StringField('Comment:')
    count = IntegerField('How many strings:')
    addbutton = SubmitField('Add')

class ChangeLicenseForm(FlaskForm):
    '''
    change license form
    '''
    software_name = StringField('Software name:')
    key = StringField('License key:')
    folder = StringField('Folder:')
    version = StringField('Version:')
    start_date = DateField('Start date:', format="%Y-%m-%d")
    end_date = DateField('Expiration date:', format="%Y-%m-%d", validators=[Optional()])
    user = StringField('Owner username:')
    comment = StringField('Comment:')
    editbutton = SubmitField('Edit')


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'Set_your-Secret3Key'

@app.route('/', methods=['GET', 'POST'])
def showall():
    form = SearchLicenseForm()
    search_results = None
    search_results = models.get_license()
    if form.validate_on_submit():
        search_results = models.get_license(software_name=form.software_name.data, end_date=form.end_date.data)
    return render_template('showall.html', form=form, search_results=search_results)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddLicenseForm()
    search_results = None
    if form.validate_on_submit():
        models.add_license(
            software_name=form.software_name.data,
            key=form.key.data,
            folder=form.folder.data,
            version=form.version.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            user=form.user.data,
            comment=form.comment.data,
            count=form.count.data
        )
        search_results = models.get_license(software_name=form.software_name.data)
    return render_template('add.html', search_results=search_results, form=form)

@app.route('/delete/<int:id>/<int:approve>', methods=['GET', 'POST'])
def delete_license(id, approve):
    '''
    Delete a license from the database
    '''
    form = SearchLicenseForm()
    if approve == 1:
        models.del_license(id)
    search_results = models.get_license(id)
    return render_template('delete.html', search_results=search_results, form=form)

@app.route('/change/<int:id>', methods=['GET', 'POST'])
def change_license(id):
    '''
    Change a license in the database
    '''
    form = ChangeLicenseForm()
    search_results = models.get_license(key_id=id)
    if form.validate_on_submit():
        models.change_license(id,
        software_name=form.software_name.data,
        key=form.key.data,
        folder=form.folder.data,
        version=form.version.data,
        start_date=form.start_date.data,
        end_date=form.end_date.data,
        user=form.user.data, 
        comment=form.comment.data
        )
        return redirect(id)
    return render_template('change.html', search_results=search_results, form=form)

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
