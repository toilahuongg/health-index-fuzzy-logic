from flask import request, Response
import jwt, os
from models import User
def Auth(func):
  def checkToken(*args, **kwargs):
    try:
      token = request.headers['Authorization']
      token = token.replace("Bearer", "").strip()
      data = jwt.decode(token, os.getenv('SECRET_KEY') or '',  algorithms=["HS256"])
      user = User.query.filter_by(id=data.get('id')).first()
      if not user:
        raise Exception
      request.userId = data.get('id') # type: ignore
      return func(*args, **kwargs)
    except:
      return Response('Authorization failed', status=401)
  checkToken.__name__ = func.__name__
  return checkToken