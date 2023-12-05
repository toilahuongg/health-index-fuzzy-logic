from datetime import datetime, timedelta
from flask import Blueprint, json, request, jsonify
import re, bcrypt, jwt, os
from helpers.files import removeFile, uploadFile
from models import User, db
from middlewares import Auth

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def checkEmail(email):
  if(re.fullmatch(regex, email)):
    return True
  return False


userRouter = Blueprint('userRouter', __name__)

@userRouter.route('/<username>', methods=['GET'])
def getUserByUsername(username):
  user = User.query.filter_by(username=username).first()
  if (not user): return jsonify({ 'error' : 'Tài khoản này không tồn tại' })
  result: dict = user.to_dict()
  result.pop('password') 
  result.pop('email') 
  return jsonify(result)

@userRouter.route('/<userId>/id', methods=['GET'])
def getUserById(userId):
  user = User.query.filter_by(id=userId).first()
  if (not user): return jsonify({ 'error' : 'Tài khoản này không tồn tại' })
  result: dict = user.to_dict()
  result.pop('password') 
  result.pop('email') 
  return jsonify(result)

