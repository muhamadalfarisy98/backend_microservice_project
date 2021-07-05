from flask import Flask
from config import Config
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)


from app.routes.parent_routes import *
from app.routes.teacher_routes import *
from app.routes.student_routes import *
from app.routes.subject_routes import *
from app.routes.class_routes import *
from app.routes.jadwal_routes import *
from app.routes.sesi_routes import *

app.register_blueprint(parent_blueprint)
app.register_blueprint(teacher_blueprint)
app.register_blueprint(student_blueprint)
app.register_blueprint(subject_blueprint)
app.register_blueprint(class_blueprint)
app.register_blueprint(jadwal_blueprint)
app.register_blueprint(sesi_blueprint)