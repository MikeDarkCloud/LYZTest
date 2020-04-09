import json
from  common.conf import *
js = '{"stdId":"158570096798115805","userId":"158570096797867814","stdName":"ATUOTEST",' \
     '"learnId":"158570096799187380","pfsnLevel":"5","stdStage":null,"inclusionStatus":null,' \
     '"accAmount":"0.00","zmAmount":"0.00","recruitType":"1","unvsName":"\u5609\u5E94\u5B66\u9662",' \
     '"grade":"2021","pfsnCode":"79895","pfsnName":"\u884C\u653F\u7BA1\u7406","orderStatus":null,' \
     '"feeName":null,"offerName":null,"stdType":null,"relation":0,"reduction":false,' \
     '"payInfos":[{"learnId":null,"itemCode":"Y0","itemName":"\u8003\u524D\u8F85\u5BFC\u8D3911",' \
     '"itemYear":"0","itemType":"1","payable":"199.00","subOrderStatus":"1","refundAmount":"0.00",' \
     '"subOrderNo":"158570096799436764","xjAmount":null,"zmAmount":null,"zlAmount":null,"yhqAmount":null,' \
     '"orderNum":0,"feeAmount":null,"offerAmount":null,"payTime":null,"payType":0,"isRefund":0,"payNo":null,' \
     '"outSerialNo":null}],"feeId":null,"nowFeeId":null,"scholarship":"69","taId":null,"pfsnId":null,' \
     '"entranceScore":null,"createTime":null,"tutorPayInfos":[{"learnId":null,"itemCode":"Y0",' \
     '"itemName":"\u8003\u524D\u8F85\u5BFC\u8D3911","itemYear":"0","itemType":"1","payable":"199.00",' \
     '"subOrderStatus":"1","refundAmount":"0.00","subOrderNo":"158570096799436764",' \
     '"xjAmount":null,"zmAmount":null,"zlAmount":null,"yhqAmount":null,"orderNum":0,"feeAmount":null,' \
     '"offerAmount":null,"payTime":null,"payType":0,"isRefund":0,"payNo":null,"outSerialNo":null}],' \
     '"firstPayInfos":[],"secondPayInfos":[],"thirdPayInfos":[],"otherPayInfos":[]}'
pay = {"learnId":"158570096799187380","paymentType":"1","tradeType":"NATIVE",
       "accDeduction":"0.00","zmDeduction":"0","coupons":"[]",
       "items":"[{\"orderNo\":\"158570096799436764\",\"itemCode\":\"Y0\",\"itemName\":\"考前辅导费11\",\"itemYear\":\"0\""
               ",\"amount\":\"199.00\",\"accScale\":0,\"zmScale\":0,\"couponScale\":0,\"payAmount\":\"199.00\"}]",
       "dataSources":"5","grade":"2021","payAmount":"199.00","remark":""}

ldict = json.loads(js)
# d = json.dumps(js)
# print(ldict['subOrderNo'])
# print(ldict)
# print(ldict['learnId'])
# print(ldict['payInfos'][0]['subOrderNo'])
# print(ldict['payInfos'][0]['payable'])
# # print(ldict['payable'])
# print(ldict['grade'])
# print(pay)


y = Config().Rallyaml('test')
print(y)







