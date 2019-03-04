# coding:utf-8
import urllib2,cookielib,urllib

login_url = 'https://www.alpharacks.com/myrack/dologin.php'
#定义登录所需要用的信息，如用户名、密码等，详见下图，使用urllib进行编码
login_data = urllib.urlencode({
                        "username": 'xxxxxx@xx.com',
                        "password": 'xxxxxxxxxxxxxx',
                        "autologin": 1,
                        "enter": "Sign in"})
#设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
cj = cookielib.CookieJar() #获取Cookiejar对象（存在本机的cookie消息）
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj)) #自定义opener,并将opener跟CookieJar对象绑定
urllib2.install_opener(opener) #安装opener,此后调用urlopen()时都会使用安装过的opener对象
response=opener.open(login_url,login_data).read() #访问登录页，自动带着cookie信息

url3 = 'https://www.alpharacks.com/myrack/modules/servers/solusvmpro/get_client_data.php?vserverid=37914&_=1551671844735'
response = opener.open(url3,None).read()
onLine =  str(response).split('strong')[1].split('>')[1].split('<')[0]
print onLine
if onLine == "Offline":
    url4 = 'https://www.alpharacks.com/myrack/clientarea.php?action=productdetails&id=48669&serveraction=custom&a=boot'
    response = opener.open(url4, None).read()

