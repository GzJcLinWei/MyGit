import tornado.web



templates_path = r"templates/"
user_name="admin"
user_password="admin"
html_title="test_files"


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        message = "demos1"
        self.render(templates_path + "test.html",html_title = html_title,
                    message = message)


class WelcomeHandler(tornado.web.RequestHandler):
    def post(self):
        name = self.get_argument(r"user_name")
        password = self.get_argument(r"user_password")
        if name == user_name and password == user_password:
            welcome = "hello!"
            self.render(templates_path + "welcome.html",html_title = html_title,
                    welcome = welcome,name = name)
        else:
            message = u"登陆失败"
            self.render(templates_path + "test.html",html_title = html_title,
                        message = message)
    def get(self):
        message = u"请先登录"
        self.render(templates_path + "test.html",html_title = html_title,
                    message = message)

