from flask import Flask
from flask_cors import CORS
import os
from routes.dataResource import DataResourceRouter
from routes.userRouter import userRouter
from routes.authRouter import authRouter
from routes.heathIndexRouter import HIRouter
from models import db
from seed import db_create, db_drop, db_reset, db_seed

app = Flask(__name__,static_url_path='', static_folder='static')
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db.init_app(app)

app.register_blueprint(userRouter, url_prefix='/api/users')
app.register_blueprint(authRouter, url_prefix='/api/auth')
app.register_blueprint(HIRouter, url_prefix='/api/heath-index')
app.register_blueprint(DataResourceRouter, url_prefix='/api/data-resource')

#Command
if not os.getenv('FLASK_ENV') == 'production':
    app.cli.command('db_create')(db_create)
    app.cli.command('db_drop')(db_drop)
    app.cli.command('db_seed')(db_seed)
    app.cli.command('db_reset')(db_reset)
    
if __name__ == '__main__':
   app.run()