import pymysql
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from .forms import nameForm
from django.views.decorators.csrf import csrf_protect
# Create your views here.
from .models import Register      # 引入models

def test1(request):
    return render(request,'app001/test1.html')

# def index1(request): #定义视图index1
#   ans={} #创建一个字典
#   ans['head']='hello ' # 赋值
#   return render(request,'app001/firstpage.html',ans) # 输出字典
  
#是定义一个index1，向'templates/app001/firstpage.html'输出字典ans的值。

# def index1(request):
#     name = request.GET.get('name1') #获取参数
#     ans = {}
#     ans['head'] ='hello,' + name
#     return render(request,'app001/firstpage.html',ans)

# @csrf_protect   
# def index1(request):
#     if request.method == 'POST': #是否为post请求
#         form=nameForm(request.POST)
#         if form.is_valid(): #检查输入是否规范，符合规范，传递变量，刷新页面
#             ans={}
#             name=form.cleaned_data['name1']
#             ans['head']=name  
#             return render(request,'app001/test1.html',ans) 
#     else:
#          return render(request,'app001/test1.html')
     
def index1(request):
    a=Register.objects.values('username')  # 查询 
    ans={}
    ans['head']=a  # 显示查询结果
    return render(request,'app001/firstpage.html',ans)


def index(request):
    return render(request, 'app001/firstpage.html')

def login_action(request):
    conn=pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123456',
        database='login',
        charset='utf8')
    cursor=conn.cursor(pymysql.cursors.DictCursor)
    if request.method == 'POST':                             #判断是否为post提交方式
        username_in = request.POST.get('username', '')          #通过post.get()方法获取输入的用户名及密码
        password_in = request.POST.get('password', '')
        sql="select * from register where username='%s' and password='%s'" %(username_in,password_in)
        result = cursor.execute(sql)
        if result:
            return HttpResponseRedirect('/event_manage/')    #如果正确，（这里调用另一个函数，实现登陆成功页面独立，使用HttpResponseRedirect()方法实现
        else:
            return render(request,'app001/firstpage.html',{'error':'username or password error.'})#不正确，通过render(request,"index.html")方法在error标签处显示错误提示

def event_manage(request):                                          #该函数定义的是成功页面的提示页面

    #username =request.COOKIES.get('user', '') #读取浏览器cookie
    return render(request,"app001/event_manage.html") #{"user":username})      　#在上面的函数判断用户名密码正确后在显示该页面，指定到event_manage.html,切换到一个新的html页面


