from flask import Blueprint, make_response, request, jsonify
from middlewares import Auth
from helpers.fuzzy import fuzzy
from models import HeathIndex, User, db

HIRouter = Blueprint('HIRouter', __name__)

@HIRouter.route('', methods=['GET'])
@Auth
def get_all_HI():
    range_values = request.args.get('range', default=None, type=str)
    start,end = 0, 20
    if range_values:
      start, end = eval(range_values)
    query = HeathIndex.query.filter_by(user_id=request.userId).order_by(HeathIndex.createdAt.desc())
    total_rows = query.count()
    HI_list = query.slice(start, end).all()
    response = make_response(jsonify([hi.to_dict() for hi in HI_list]))
    response.headers['Content-Range'] = f'heath-index {start}-{end}/{total_rows}'
    response.headers['Access-Control-Expose-Headers'] = 'Content-Range'
    return response

@HIRouter.route('', methods=['POST'])
@Auth
def createHeathIndex():
  try:
    chieu_cao = float(request.json.get('chieu_cao') or '0')
    can_nang = float(request.json.get('can_nang') or '0')
    mat = float(request.json.get('mat') or '0')
    rang = float(request.json.get('rang') or '0')
    suc_nghe = float(request.json.get('suc_nghe') or '0')
    mach = float(request.json.get('mach') or '0')
    co_rut = float(request.json.get('co_rut') or '0')
    
    user = User.query.filter_by(id=request.userId).first()


    point1,point2,point3,point4,point5,point6 = fuzzy(
      chieu_cao=chieu_cao,
      can_nang=can_nang,
      mat=mat,
      rang=rang,
      suc_nghe=suc_nghe,
      mach=mach,
      co_rut=co_rut
    )

    HI = HeathIndex(
      chieu_cao=chieu_cao,
      can_nang=can_nang,
      mat=mat,
      rang=rang,
      suc_nghe=suc_nghe,
      mach=mach,
      co_rut=co_rut,
      point1=point1,
      point2=point2,
      point3=point3,
      point4=point4,
      point5=point5,
      point6=point6,
      user=user
    )
    db.session.add(HI)
    try:
      db.session.commit()
    except: 
      return jsonify({'error': 'Đã xảy ra lỗi'}), 500

    return jsonify(HI),200
  except NameError:
    return jsonify({'error': 'Đã xảy ra lỗi'}), 400
  
@HIRouter.route('/<id>', methods=['GET'])
def getHIByID(id):
  HI = HeathIndex.query.filter_by(id=id).first()
  if (not HI): return jsonify({ 'error' : 'Tài khoản này không tồn tại' })
  return jsonify(HI.to_dict())