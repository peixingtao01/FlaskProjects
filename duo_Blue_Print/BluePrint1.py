from flask import Blueprint

blueprint_simple1 = Blueprint('blueprint_simpleya1',__name__)

@blueprint_simple1.route('/index1')
def index():
    return 'blueprint_simple1'



