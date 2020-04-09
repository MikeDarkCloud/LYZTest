import re
def regx(context,patt):
    pattern = re.compile(patt)
    result = re.findall(pattern, context, flags=0)
    return result






# text ='{"code":"00","body":{"data":[{"pfsnId":"153836535253022863","pfsnName":"航空航天","pfsnCode":"100101","pfsnLevel":"5","year":"2020"},{"pfsnId":"153836539871974180","pfsnName":"软件开发","pfsnCode":"100102","pfsnLevel":"5","year":"2020"},{"pfsnId":"153836544109862031","pfsnName":"太空探索","pfsnCode":"100103","pfsnLevel":"5","year":"2020"}],"recordsTotal":3,"recordsFiltered":3},"msg":"","ok":true}'
text ='var row = {"stdId":"158570096798115805","userId":"158570096797867814","stdName":"ATUOTEST","learnId":"158570096799187380","pfsnLevel":"5","stdStage":null,"inclusionStatus":null,"accAmount":"0.00","zmAmount":"0.00","recruitType":"1","unvsName":"\u5609\u5E94\u5B66\u9662","grade":"2021","pfsnCode":"79895","pfsnName":"\u884C\u653F\u7BA1\u7406","orderStatus":null,"feeName":null,"offerName":null,"stdType":null,"relation":0,"reduction":false,"payInfos":[{"learnId":null,"itemCode":"Y0","itemName":"\u8003\u524D\u8F85\u5BFC\u8D3911","itemYear":"0","itemType":"1","payable":"199.00","subOrderStatus":"1","refundAmount":"0.00","subOrderNo":"158570096799436764","xjAmount":null,"zmAmount":null,"zlAmount":null,"yhqAmount":null,"orderNum":0,"feeAmount":null,"offerAmount":null,"payTime":null,"payType":0,"isRefund":0,"payNo":null,"outSerialNo":null}],"feeId":null,"nowFeeId":null,"scholarship":"69","taId":null,"pfsnId":null,"entranceScore":null,"createTime":null,"tutorPayInfos":[{"learnId":null,"itemCode":"Y0","itemName":"\u8003\u524D\u8F85\u5BFC\u8D3911","itemYear":"0","itemType":"1","payable":"199.00","subOrderStatus":"1","refundAmount":"0.00","subOrderNo":"158570096799436764","xjAmount":null,"zmAmount":null,"zlAmount":null,"yhqAmount":null,"orderNum":0,"feeAmount":null,"offerAmount":null,"payTime":null,"payType":0,"isRefund":0,"payNo":null,"outSerialNo":null}],"firstPayInfos":[],"secondPayInfos":[],"thirdPayInfos":[],"otherPayInfos":[]};'
# # patt = r'"cityCode":"(.+?)"'
patt = r'var row = (.+?);'
# patt = r'"pfsnId":"(.+?)","pfsnName":"(.+?)","pfsnCode":"(.+?)"'
print(regx(text,patt))
# print(regx(text,patt)[0])
# print(regx(text,patt)[1])
# print(regx(text,patt)[2])


