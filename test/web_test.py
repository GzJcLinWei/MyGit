import tornado.ioloop
import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        s="demos1"
        self.render("test.html",s=s)

class WelCome(tornado.web.RequestHandler):
    def post(self):
        name=self.get_argument(r"user_name")
        password=self.get_argument(r"user_password")
        if name==Name and password==Pass:
            title="welcome!"+name
            self.render("welcome.html",name=name,title=title)
        else:
            s="登陆失败"
            self.render("test.html",s=s)
    def get(self):
        s="请先登录"
        self.render("test.html",s=s)
application = tornado.web.Application([
    (r"/",MainHandler),(r"/welcome",WelCome)
])
if __name__ == "__main__":
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
