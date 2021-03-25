from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config')
CORS(app)

@app.errorhandler(404)
def not_found(error):
    return jsonify({ 'Success': 'false', 'Data': { 'Message': 'Request Not Found Error' }}), 404

# Import Controllers
from App.Controller.WetherController import wetherController
# Register Controllers
app.register_blueprint(wetherController)
