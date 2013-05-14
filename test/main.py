import tornado.ioloop
import tornado.web
import handlers



application = tornado.web.Application([
    (r"/",handlers.MainHandler),
    (r"/welcome",handlers.WelcomeHandler),
    (r"/logon",handlers.Logon)
])


if __name__ == "__main__":
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
