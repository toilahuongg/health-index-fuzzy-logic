import os
from random import randrange
import time
import lorem
import requests
from helpers.files import UPLOAD_FOLDER, optimizeFile, removeAllFile
from helpers.slug import slug
from datetime import datetime
from faker import Faker
import random
fake = Faker()
from models import HeathIndex, db, User
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
sizes = ['1600/900', '1600/1200', '1200/1600', '600/900', '1200/1000']
def db_drop():
    db.drop_all()
    removeAllFile()
    print('Database dropped!')
def db_create():
    db.create_all()
    print('Database created!')
def db_seed():
    start = time.time()
    listSeed = []

    
    userAdmin = User(
        username="admin",
        fullname="admin",
        password="$2b$12$RO5ip9d.uRNo6qgnAdboTe0ucmif5DrqfFhqFs0AiJ.oOwiO7sQby",
        email="admin@gmail.com",
        gender="male",
    )
    listSeed.append(userAdmin)
    
    userMember = User(
        username="member",
        fullname="member",
        password="$2b$12$RO5ip9d.uRNo6qgnAdboTe0ucmif5DrqfFhqFs0AiJ.oOwiO7sQby",
        email="member@gmail.com",
        gender="male",
    )
    listSeed.append(userMember)
    db.session.add_all(listSeed)
    db.session.commit()

    for _ in range(1000):
        fake_data = {
            'chieu_cao': fake.random_int(min=150, max=180),
            'can_nang': fake.random_int(min=50, max=100),
            'mat': fake.random_int(min=0, max=20),
            'rang': fake.random_int(min=0, max=10),
            'suc_nghe': fake.random_int(min=1, max=20),
            'mach': fake.random_int(min=60, max=120),
            'co_rut': fake.random_int(min=0, max=5),
            'point1': fake.random_number(2),
            'point2': fake.random_number(2),
            'point3': fake.random_number(2),
            'point4': fake.random_number(2),
            'point5': fake.random_number(2),
            'point6': fake.random_number(2),
            'user_id': 1,
            'createdAt': fake.date_time_this_decade(),
            'updatedAt': fake.date_time_this_month()
        }
        heath_index = HeathIndex(**fake_data)
        db.session.add(heath_index)

    # Commit the changes to the database
    db.session.commit()
    end = time.time()
    print('Database seed!')
    print(f'{bcolors.OKBLUE}Time: {bcolors.OKGREEN} {"{:.2f}s".format(end-start)}{bcolors.ENDC}')
def db_reset():
    db_drop()
    db_create()
    db_seed()
    print(f'{bcolors.OKGREEN}Database reset!{bcolors.ENDC}')