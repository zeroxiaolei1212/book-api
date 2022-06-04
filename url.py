from views.user import UserRegister, UserLogin, UserInfo

class urlManage():
    # 这是默认的，必须要有的
    def __init__(self) -> None:
        pass

    @staticmethod
    def init_url(api):
        api.add_resource(UserRegister,'/user/register')
        api.add_resource(UserLogin,'/user/login')
        api.add_resource(UserInfo, '/user/info/<int:id>')