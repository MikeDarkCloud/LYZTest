import re
def regx(context,patt):
    pattern = re.compile(patt)
    result = re.findall(pattern, context, flags=0)
    return result






# text ='{"code":"00","body":{"data":[{"pfsnId":"153836535253022863","pfsnName":"航空航天","pfsnCode":"100101","pfsnLevel":"5","year":"2020"},{"pfsnId":"153836539871974180","pfsnName":"软件开发","pfsnCode":"100102","pfsnLevel":"5","year":"2020"},{"pfsnId":"153836544109862031","pfsnName":"太空探索","pfsnCode":"100103","pfsnLevel":"5","year":"2020"}],"recordsTotal":3,"recordsFiltered":3},"msg":"","ok":true}'
# # patt = r'"cityCode":"(.+?)"'
# patt = r'"pfsnId":"(.+?)","pfsnName":"(.+?)","pfsnCode":"(.+?)"'
# print(regx(text,patt))
# print(regx(text,patt)[0])
# print(regx(text,patt)[1])
# print(regx(text,patt)[2])


