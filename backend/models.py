from dataclasses import dataclass
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

IGNORE_FIELD = ['password', 'query', 'query_class', 'registry']
@dataclass
class User(db.Model):
  __tablename__ = 'users'
  id: int
  username: str
  password: str
  fullname: str
  email: str
  gender: str
  introduce: str
  avatar: str
  cover: str
  createdAt: datetime
  updatedAt: datetime

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username = db.Column(db.String(100), unique=True, nullable=False)
  password = db.Column(db.String(100), nullable=False)
  fullname = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(100), unique=True, nullable=False)
  gender = db.Column(db.String(100), nullable=False)
  introduce = db.Column(db.String(), nullable=True)
  avatar = db.Column(db.String(), nullable=True)
  cover = db.Column(db.String(), nullable=True)
  HeathIndexList = db.relationship('HeathIndex', backref='user', lazy=True, passive_deletes="all")  
  createdAt = db.Column(db.DateTime, default=db.func.now())
  updatedAt = db.Column(db.DateTime, default=db.func.now(), server_onupdate=db.func.now())

  def to_dict(self):
    return {key: getattr(self, key) for key in self.__annotations__.keys()}

@dataclass
class HeathIndex(db.Model):
  __tablename__ = 'heathIndexTb'
  id: int
  chieu_cao: float
  can_nang: float
  mat: float
  rang: float
  suc_nghe: float
  mach: float
  co_rut: float
  point1: float
  point2: float
  point3: float
  point4: float
  point5: float
  point6: float
  createdAt = db.Column(db.DateTime, default=db.func.now())
  updatedAt = db.Column(db.DateTime, default=db.func.now(), server_onupdate=db.func.now())

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  chieu_cao = db.Column(db.Float, nullable=False)
  can_nang = db.Column(db.Float, nullable=False)
  mat = db.Column(db.Float, nullable=False)
  rang = db.Column(db.Float, nullable=False)
  suc_nghe = db.Column(db.Float, nullable=False)
  mach = db.Column(db.Float, nullable=False)
  co_rut = db.Column(db.Float, nullable=True)
  point1 = db.Column(db.Float, nullable=False)
  point2 = db.Column(db.Float, nullable=False)
  point3 = db.Column(db.Float, nullable=False)
  point4 = db.Column(db.Float, nullable=False)
  point5 = db.Column(db.Float, nullable=False)
  point6 = db.Column(db.Float, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
  createdAt = db.Column(db.DateTime, default=db.func.now())
  updatedAt = db.Column(db.DateTime, default=db.func.now(), server_onupdate=db.func.now())
  def to_dict(self):
    _dict = {key: getattr(self, key) for key in self.__annotations__.keys()}
    points = [self.point1, self.point2, self.point3, self.point4, self.point5, self.point6]
    maxPoint = max(points)
    indexResult = points.index(maxPoint) + 1
    _dict['ket_qua'] = indexResult
    _dict['created_at'] = self.createdAt.strftime('%Y-%m-%d %H:%M:%S')
    return _dict
  def to_data_resource(self, prop):
    _dict = {}
    _dict[prop] = self[prop]
    _dict['created_at'] = self.createdAt.strftime('%Y-%m-%d %H:%M:%S')
    return _dict