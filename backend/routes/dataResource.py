from flask import Blueprint, make_response, request, jsonify
from middlewares import Auth
from helpers.fuzzy import fuzzy
from models import HeathIndex, db

DataResourceRouter = Blueprint('DataResourceRouter', __name__)

@DataResourceRouter.route('', methods=['GET'])
@Auth
def get_data_resource_list():
    query = HeathIndex.query.filter_by(user_id=request.userId).order_by(HeathIndex.createdAt.desc())
    HI_list = query.all()
    return jsonify([hi.to_dict() for hi in HI_list])