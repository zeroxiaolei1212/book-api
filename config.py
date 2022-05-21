from distutils.command.config import config


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    @staticmethod
    def init_app(app):
        pass

# 开发环境 语法：mysql+pymysql://用户名：密码@ip：端口/数据库名
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234567890@localhost:3306/bookdb'

# 生产环境 语法：mysql+pymysql://用户名：密码@ip：端口/数据库名
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234567890@localhost:3306/bookdb'

# 配置字典
config = {
    'Development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}