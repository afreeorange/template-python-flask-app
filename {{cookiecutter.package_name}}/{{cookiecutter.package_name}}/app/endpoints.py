from flask import render_template
from . import {{cookiecutter.package_name}}_blueprint


@{{cookiecutter.package_name}}_blueprint.route('/')
def index():
    return render_template('index.html')
