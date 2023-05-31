from flask import Flask
from flask_sqlalchemy import SQLAlchemy, session
from config import DATABASE


# 创建Flask应用程序实例
app = Flask(__name__)

# 配置Flask应用程序
app.config['SQLALCHEMY_DATABASE_URI'] = f"{DATABASE['ENGINE']}://{DATABASE['URI']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# 创建SQLAlchemy对象
db = SQLAlchemy(app)

# 注册蓝图
from routes import routes_bp

app.register_blueprint(routes_bp)


