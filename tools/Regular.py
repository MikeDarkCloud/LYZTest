import re
def regx(context,patt):
    pattern = re.compile(patt)
    return re.findall(pattern, context, flags=0)






text ="var appidString='wx4acabbb70612e297';var redirectUriString='http://bms.yzwill.cn';var hrefString='https://static.yzou.cn/css/wxLogin.css';"
patt = r"appidString='(.+?)';"
print(regx(text,patt))