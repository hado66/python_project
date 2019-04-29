name='wzy'
password='123'

def auth(func):
    def warpper(*args,**kwargs):
        username=input(">>name: ")
        passwd=input(">>password: ")
        # if username==name and passwd==password:
        if True:
            res=func(*args,**kwargs)
            return res
        else:
            print("用户名或密码错误")
    return warpper



def index():
    print("in the index 首页")

@auth
def home(name):
    print("%s后台欢迎您 "%name)
    return '这个是测试 return '

@auth
def login():
    print('登录')



# c=home('dddd')
# print(c)

login()

