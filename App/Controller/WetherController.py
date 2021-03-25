from flask import Blueprint, jsonify
from App.Repository.WetherRepository import WetherRepository
wetherController = Blueprint('wether', __name__, url_prefix='/api/wether')

class WetherController():
    def __init__(self):
        pass

    @wetherController.route('/', methods=['GET'])
    def GetWether():
        repository = WetherRepository()
        response = repository.GetWether()
        
        return jsonify(response.__dict__)