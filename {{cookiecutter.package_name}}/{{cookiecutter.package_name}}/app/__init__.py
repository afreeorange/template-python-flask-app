from flask import Blueprint

{{cookiecutter.package_name}}_blueprint = Blueprint(
    '{{cookiecutter.package_name}}_blueprint',
    __name__,
    template_folder='./templates',
    static_folder='./static',
    static_url_path='/app/static',
)

from . import endpoints
