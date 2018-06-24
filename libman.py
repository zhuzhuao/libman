#coding:utf-8
import pymysql
import string
import getpass
import os
import time
from datetime import date
class book(object):
    name = None
    author = None
    id = None
    price = 0.0
    had = 0
class student(object):
    name = None
    sno = None
    sex = None
    tel = None
    major = None
    classes = None
def login():
    os.system('cls')
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         passwd='weiruyi123',
                         db='libman',
                         charset = 'utf8'
                         )
    cu = db.cursor()
    uname = str(input("请输入用户名:"))
    pwd = str(getpass.getpass("请输入密码:"))
    r = cu.execute('select account from admin where account = %s',(uname))
    if r == 1:
        re = cu.execute('select pwd from admin where account = %s',(uname))
        upwd = cu.fetchmany()[0][0]
        if pwd == upwd:
            os.system('cls')
            print('登陆成功^_^')
            db.close()
            time.sleep(1)
            return uname
        else:
            os.system('cls')
            print('用户名或密码错误。。。。')
            time.sleep(1)
            return 0
    else:
        os.system('cls')
        print("用户名或密码错误。。。。")
        time.sleep(1)
        return 0
def add_admin():
    account = input('输入新用户名:')
    pwd = input('输入新用户名的密码:')
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         passwd='weiruyi123',
                         db='libman',
                         charset = 'utf8'
                         )
    cu = db.cursor()
    r = cu.execute('select account from admin where account = %s', (account))
    if r == 0:
        cu.execute("insert into admin(account,pwd) values(%s,%s)", (account,pwd))
        print('添加用户' + account + '成功')
        db.commit()
        cu.close()
        db.close()
        time.sleep(1)
    else:
        print("用户名已存在。。")
        db.close()
        time.sleep(1)
def search_book(bname):
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         passwd='weiruyi123',
                         db='libman',
                         charset='utf8'
                         )
    cu = db.cursor()
    cu.execute("select * from books where bname LIKE '%{}%' or author LIKE '%{}%' or bnum like '{}'".format(bname,bname,bname))
    return cu.fetchall()
def search_student(sname):
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         passwd='weiruyi123',
                         db='libman',
                         charset = 'utf8'
                         )
    cu = db.cursor()
    cu.execute("select * from students where sname = '{}' or sno = '{}'".format(sname,sname))
    return cu.fetchall()
def add_del_book():
    print('\t\t\t\t\t  1.添加书籍')
    print('\t\t\t\t\t  2.删除书籍')
    print('\t\t\t\t\t  3.返回上一页')
    choice = str(input("选择操作:"))
    if choice == '1':
        add_book()
    elif choice == '2':
        del_book()
    elif choice == '3':
        return 0
    else:
        os.system('cls')
        print('输入的选项有误，请重新输入')
        time.sleep(1)
        os.system('cls')
        add_del_book()
def add_book():
    os.system('cls')
    books = book()
    books.name = str(input('书籍名称:'))
    books.author = str(input('书籍作者:'))
    books.id = str(input('书籍编号:'))
    books.price = str(input('书籍价格:'))
    books.had = int(input('书籍本书:'))
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         passwd='weiruyi123',
                         db='libman',
                         charset = 'utf8'
                         )
    cu = db.cursor()
    if len(search_book(books.name)) == 0:
        cu.execute('insert into books(bname,author,bnum,bprices,had) values(%s,%s,%s,%s,%s)',('《' + books.name + '》',books.author,books.id,books.price + '元',str(books.had) + '本'))
        print("书名:" + books.name + "\n作者:" + books.author + "\n编号:" + books.id + "\n价格:" + books.price + "\n剩余本书:" + str(books.had) + "\n")
        ans = input('\n确认无误(y/n):')
        if ans == 'y' or ans == 'Y':
            db.commit()
            cu.close()
            db.close()
            print('\n录入成功!!!')
            os.system('pause')
        else:
            os.system('cls')
            add_del_book()
    else:
        print("\n书籍已存在....")
        time.sleep(1)
        os.system('cls')
        add_del_book()
def show_all_book():
    os.system('cls')
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         passwd='weiruyi123',
                         db='libman',
                         charset='utf8'
                         )
    cu = db.cursor()
    cu.execute('select * from books')
    for i in cu.fetchall():
        print("书名:" + i[0] + "\n作者:" + i[1] + "\n编号:" + i[2] + "\n价格:" + str(i[3]) + "\n剩余本书:" + str(i[4]) + "\n")
def del_book():
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         passwd='weiruyi123',
                         db='libman',
                         charset = 'utf8'
                         )
    cu = db.cursor()
    show_all_book()
    books = str(input('输入你想删除的书的书名:'))
    re = search_book(books)
    if len(re) != 0:
        os.system('cls')
        for i in re:
            print("书名:" + i[0] + "\n作者:" + i[1] + "\n编号:" + i[2] + "\n价格:" + str(i[3]) + "\n剩余本书:" + str(i[4]) + "\n")
            ans = input('\n确认删除(y/n):')
            if ans == 'y' or ans == 'Y':
                cu.execute("delete from books where bname like '《{}》'".format(books))
                db.commit()
                cu.close()
                db.close()
                print('\n删除成功!!!')
                os.system('pause')
    else:
        print('\n没有找到所输入的书籍。。。\n')
        time.sleep(1)
        os.system('pause')
def broww_back_book():
    print('\t\t\t\t\t  1.借阅书籍')
    print('\t\t\t\t\t  2.归还书籍')
    print('\t\t\t\t\t  3.返回上一页')
    choice = str(input("选择操作:"))
    if choice == '1':
        brow_book()
    elif choice == '2':
        reback_book()
    elif choice == '3':
        return 0
    else:
        os.system('cls')
        print('输入的选项有误，请重新输入')
        time.sleep(1)
        os.system('cls')
        broww_back_book()
def brow_book():
    student = str(input("输入学生的学号或姓名:"))
    sre = search_student(student)
    if len(sre) != 0:
        show_all_book()
        books = input('输入你想借阅的书籍的书名或编号:')
        bre = search_book(books)
        db = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             passwd='weiruyi123',
                             db='libman',
                             charset = 'utf8'
                             )
        cu = db.cursor()
        if len(bre) != 0:
            os.system('cls')
            if int(bre[0][4][:-1]) != 0:
                for i in bre:
                    print("书名:" + i[0] + "\n作者:" + i[1] + "\n编号:" + i[2] + "\n价格:" + str(i[3]) + "\n剩余本书:" + str(i[4]) + "\n")
                    ans = input('\n确认借阅(y/n):')
                    if ans == 'y' or ans == 'Y':
                        while True:
                            days = input("输入借阅天数(小于30天):")
                            if days.isdigit() or (days <= 30 and days > 0):
                                break
                            else:
                                print("输入天数不符合要求...")
                        had = int(bre[0][4][:-1])
                        bname = str(bre[0][0])
                        bsno = str(sre[0][1])
                        sname = str(sre[0][0])
                        times = date.today()
                        btime = times
                        outline = 0
                        cu.execute('insert into logs(bname,bsno,btime,howlong,outline) values (%s,%s,%s,%s,%s)',(bname,bsno,str(times),str(days) + '天',str(outline) + '天'))
                        cu.execute("update books set had = '{}' where bname = '{}'".format(str(had - 1)+'本',bname))
                        db.commit()
                        cu.close()
                        db.close()
                        print('\n借阅成功!!!')
                        os.system('pause')
                    else:
                        os.system('cls')
                        print('\t\t\t\t\t图书借阅/归还')
                        broww_back_book()
            else:
                print("所选书籍已没有存库。。。抱歉。")
                os.system('cls')
                print('\t\t\t\t\t图书借阅/归还')
                broww_back_book()
        else:
            print('\n没有找到所输入的书籍。。。\n')
            time.sleep(1)
            os.system('pause')
            os.system('cls')
            print('\t\t\t\t\t图书借阅/归还')
            broww_back_book()
    else:
        print('\n没有找到输入的学生。。。\n')
        time.sleep(1)
        os.system('pause')
        os.system('cls')
        print('\t\t\t\t\t图书借阅/归还')
        broww_back_book()
def show_stu_logs(sno):
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         passwd='weiruyi123',
                         db='libman',
                         charset = 'utf8'
                         )
    cu = db.cursor()
    cu.execute("select * from logs where bsno = '{}'".format(sno))
    return cu.fetchall()
def reback_book():
    os.system('cls')
    student = str(input("输入学生的学号或姓名:"))
    sre = search_student(student)
    books = []
    if len(sre) != 0:
        bname = sre[0][0]
        bsno = sre[0][1]
        logs = show_stu_logs(bsno)
        db = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             passwd='weiruyi123',
                             db='libman',
                             charset = 'utf8'
                             )
        cu = db.cursor()
        os.system('cls')
        for log in logs:
            cu.execute("select bnum from books where bname = '{}'".format(log[0]))
            print(cu.fetchall())
            print("借阅者:{}\n学号:{}\n借阅书籍:{}\n借阅时间:{}\n借阅时长:{}\n借阅状态:{}\n".format(bname,bsno,log[0],log[2],log[3],log[4]))
            books.append(log[0])
        os.system('pause')
        book = input('输入要归还的书的书名或编号:')
        cu.execute("select bname from books where bname = '{}' or bnum = '{}' or bname like '{}'".format(book,book,book))
        print(cu.fetchall())
        os.system('pause')
        if book in books:
            cu.execute("update logs set outline = '已归还' where bname")
        else:
            pass
    else:
        os.system('cls')
        print('输入的学生信息有误。。。')
        os.system('pause')
        os.system('cls')
        broww_back_book()
def change_pwd(a):
    i = 0
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         passwd='weiruyi123',
                         db='libman'
                         )
    cu = db.cursor()
    cu.execute("select pwd from admin where account = '{}'".format(a))
    oldpwd = cu.fetchall()
    while i<3:
        pwd = str(getpass.getpass("请输入用户{}的密码:".format(a)))
        if pwd == oldpwd[0][0]:
            os.system('cls')
            while True:
                pwd = str(getpass.getpass("请输入用户{}的新密码:".format(a)))
                pwd1 = str(getpass.getpass("请再次输入用户{}的新密码:".format(a)))
                if pwd == pwd1:
                    cu.execute("update admin set pwd = '{}' where account = '{}'".format(pwd,a))
                    db.commit()
                    cu.close()
                    db.close()
                    os.system('cls')
                    print('管理员{}密码修改成功。。请重新登陆。'.format(a))
                    os.system('pause')
                    os.system('cls')
                    login()
                    break
                else:
                    os.system('cls')
                    print("两次输入的密码不一致，请重新输入。。。")
                    os.system('pause')
                    os.system('cls')
            break
        else:
            os.system('cls')
            print("输入管理员{}的密码错误。。".format(a))
            os.system('pause')
            os.system('cls')
            i += 1
    if i == 3:
        os.system('cls')
        print("多次错误。。。退出。。")
        os.system('pause')
        os._exit(0)
def menu(role):
    print("\t\t---------------------图书管理系统---------------------")
    print("\t\t\t\t    by .adel & 2316")
    print('\t\t\t\t      '+ str(date.today()))
    if role != 'student':
        print('\t\t\t\t   1.修改管理员密码') #增
        print('\t\t\t\t   2.图书查询') #查
        print('\t\t\t\t   3.添加/删除 书籍') #增,删
        print('\t\t\t\t   4.图书借阅/归还') #增,改
        print('\t\t\t\t   5.退出')
        choice = input('请选择:')
        return choice
    else:
        print('\t\t\t\t   1.修改密码')
        print('\t\t\t\t   2.图书查询')
        print('\t\t\t\t   3.图书借阅/归还')
        print('\t\t\t\t   4.退出')
        choice = input('请选择:')
        if choice == '4':
            choice = '5'
        if choice == '3':
            choice = '4'
        return choice
def get_role(name):
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         passwd='weiruyi123',
                         db='libman',
                         charset='utf8'
                         )
    cu = db.cursor()
    cu.execute("select role from admin where account = '{}'".format(name))
    return cu.fetchall()[0][0]
i = 0
while i < 3:
    a = login()
    if type(a) == str:
        role = get_role(a)
        break
    else:
        i += 1
if i == 3:
    os.system('cls')
    print('不知道密码就别猜啦。。。-_-')
    os._exit(0)
os.system('cls')
while True:
    print('当前登录用户:{}'.format(a))
    print('身份:{}'.format(role))
    choice = menu(role)
    if choice=='1':
        os.system('cls')
        print('\t\t\t\t\t管理员密码修改')
        change_pwd(a)
        os.system('cls')
    elif choice =='2':
        os.system('cls')
        print('\t\t\t\t\t图书查询')
        bname = input('输入书籍名称或者作者:')
        result = search_book(bname)
        if len(result) != 0:
            os.system('cls')
            for i in result:
                print("书名:" + i[0] + "\n作者:" + i[1] + "\n编号:" + i[2] + "\n价格:" + str(i[3]) + "\n剩余本书:" + str(i[4]) + "\n")
            os.system('pause')
        else:
            os.system('cls')
            print('没有相关的书籍。。。')
            time.sleep(1)
        os.system('cls')
    elif choice =='3':
        if role == 'student':
            print('输入的选项无效,请重新输入。。。')
            time.sleep(1)
            os.system('cls')
            continue
        os.system('cls')
        print('\t\t\t\t\t添加/删除 书籍')
        add_del_book()
        os.system('cls')
    elif choice =='4':
        os.system('cls')
        print('\t\t\t\t\t图书借阅/归还')
        broww_back_book()
        os.system('cls')
    elif choice =='5':
        os.system('cls')
        print("正在退出。。。。")
        time.sleep(1)
        os.system('cls')
        break
    else:
        print('输入的选项无效,请重新输入。。。')
        time.sleep(1)
        os.system('cls')
os.system('exit')