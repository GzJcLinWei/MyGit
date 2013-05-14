import tornado.web
import page



request=tornado.web.RequestHandler
templates_path = r"templates/"
user_name="admin"
user_password="admin"
html_title="test_files"
test_list={1:"一",2:"二",3:"三",4:"四",5:"五",
           6:"六",7:"七",8:"八",9:"九",10:"十",
           11:"十一",12:"十二",13:"十三",14:"十四",15:"十五",
           16:"十六",17:"十七",18:"十八",19:"十九",20:"二十",
           21:"二十一",22:"二十二",23:"二十三",24:"二十四",25:"二十五",
           26:"二十六",27:"二十七",28:"二十八",29:"二十九",30:"三十",
           31:"三十一",32:"三十二",33:"三十三",34:"三十四",35:"三十五",
           36:"三十六",37:"三十七",38:"三十八",39:"三十九",40:"四十",
           41:"四十一",42:"四十二",43:"四十三",44:"四十四",45:"四十五",
           46:"四十六",47:"四十七",48:"四十八",49:"四十九",50:"五十",}


class MainHandler(request):
    def get(self):
        message = "demos1"
        self.render(templates_path + "test.html",html_title = html_title,
                    message = message)


class Logon(request):
    def post(self):
        name = self.get_argument(r"user_name")
        password = self.get_argument(r"user_password")
        if name == user_name and password == user_password:
            self.redirect(r"welcome?i=1&a=1",permanent=True)
        else:
            message = u"登陆失败"
            self.render(templates_path + "test.html",html_title = html_title,
                        message = message)
    def get(self):
        message = u"请先登录"
        self.render(templates_path + "test.html",html_title = html_title,
                    message = message)


class WelcomeHandler(request):
    def post(self):
        pass
    def get(self):
            i=int(self.get_argument(r"i"))
            rows=5 #分页的行数
            total=len(test_list)#信息总数
            pages=page.page(total,rows)#总页数
            a=int(self.get_argument(r"a"))
            self.render(templates_path + "welcome.html",
                        html_title = html_title,
                        test_list=test_list,
                        pages=pages,
                        i=i,#当前页
                        a=a,
                        rows=rows,
                        )

