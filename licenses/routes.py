from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import Required
from flask_script import Manager
import models


class SearchLicenseForm(FlaskForm):
    '''
    search licenses
    '''
    software_name = StringField('Enter software name:', validators=[Required()])
    # submit button
    searchbutton = SubmitField('Search')

class AddLicenseForm(FlaskForm):
    '''
    add license
    '''
    software_name = StringField('Software name:', validators=[Required()])
    key = StringField('License key:')
    folder = StringField('Folder:')
    version = StringField('Version:')
    start_date = DateField('Start date:', validators=[Required()], format="%d.%m.%Y")
    end_date = DateField('Expiration date:', format="%d.%m.%Y")
    user = StringField('Owner username:', validators=[Required()])
    comment = StringField('Comment:')
    # submit button
    searchbutton = SubmitField('Add')


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'Set_your-Secret3Key'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showall', methods=['GET', 'POST'])
def showall():
    all_licenses = models.get_all_licenses()
    return render_template('showall.html', all_licenses=all_licenses)

@app.route('/search', methods=['GET', 'POST'])
def socket():
    form = SearchLicenseForm()
    search_results = None
    if form.validate_on_submit():
        search_results = models.get_license_by_name(form.software_name.data)
    return render_template('search.html', search_results=search_results, form=form)

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
            comment=form.comment.data
        )
        search_results = models.get_license_by_name(form.software_name.data)
        flash('License have been added!')
    return render_template('add.html', search_results=search_results, form=form)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_license(id):
    """
    Delete a license from the database
    """
    models.del_license(id)
    all_licenses = models.get_all_licenses()
    flash('You have successfully deleted the license.')
    return render_template('showall.html', all_licenses=all_licenses)

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
