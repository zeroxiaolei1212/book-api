import os
from flask_script import Server,Manager
from flask_migrate import MigrateCommand, Migrate
from flask import Flask
from flask_restful import Api

from config import config
from db import db
from url import urlManage

# 获取config中的环境路径
config_name = os.environ.get('FLASK_CONFIG') or 'default'
app = Flask(config_name)
app.config.from_object(config[config_name] or config['default'])
api = Api(app)

# 添加命令 启动命令
manage = Manager(app)
manage.add_command("runserver", Server(use_debugger=True))
# 添加 db 命令，并与 MigrateCommand 绑定
# Migrate（）迁移
migrate = Migrate()
# 迁移与db绑定
manage.add_command('db',MigrateCommand)

if __name__ == '__main__':
    db.init_app(app)
    urlManage.init_url(api)
    migrate.init_app(app,db)
    manage.run()