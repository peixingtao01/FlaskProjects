from flask import Blueprint

blueprint_simple2 = Blueprint('blueprint_simpleya2',__name__)

@blueprint_simple2.route('/index2')
def index():
    return 'blueprint_simple2'

