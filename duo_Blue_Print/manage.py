from flask import Flask
from duo_Blue_Print.BluePrint1 import blueprint_simple1
from duo_Blue_Print.BluePrint2 import blueprint_simple2
if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(blueprint_simple1)
    app.register_blueprint(blueprint_simple2)
    app.run()



