from flask_script import Manager,Server
from app import create_app,db
from app.models import User, Role ,Blog
from flask import Flask
from  flask_migrate import Migrate, MigrateCommand

app = create_app('development')



manager = Manager(app)
manager.add_command('server',Server)



migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


@manager.shell
def make_shell_context():
   return dict(app = app,db = db,User = User,Role = Role,Blog = Blog)


if __name__ == "__main__":
  app.secret_key = '1234'
  manager.run()
