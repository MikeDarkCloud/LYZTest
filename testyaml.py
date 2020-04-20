# import yaml
#
# d = ((('aa', 'bb', 'cc','ww','qq'), ('dd', 'ee', 'ff','rr','ee'), ('jj', 'hh', 'ii','zz','xx')), ([1234], '13', '14'))
#
#
# # d[0] = ,xx(('aa','bb','cc'),('dd','ee','ff'),('jj','hh','ii'))
#
# def jiexi(Yaml, tu: tuple):
#     K=0
#     if len(tu[0]) != len(tu[1]):
#         raise Exception ("参数错误！")
#     if isinstance(tu[0], tuple):  # (('aa','bb','cc'),('dd','ee','ff'),('jj','hh','ii'))
#         for i in tu[1]:
#             # 取出一个d[0][0]('aa','bb','cc')
#             if isinstance(tu[0][K], tuple):  # ('aa','bb','cc')
#                 if len(tu[0][K]) == 1:
#                     Yaml[tu[0][K][0]] = i
#
#                 if len(tu[0][K]) == 2:
#                     Yaml[tu[0][K][0]][tu[0][K][1]] = i
#
#                 if len(tu[0][K]) == 3:
#                     Yaml[tu[0][K][0]][tu[0][K][1]][tu[0][K][2]] = i
#
#                 if len(tu[0][K]) == 4:
#                     Yaml[tu[0][K][0]][tu[0][K][1]][tu[0][K][2]][tu[0][K][3]] = i
#
#                 if len(tu[0][K]) == 5:
#                     Yaml[tu[0][K][0]][tu[0][K][1]][tu[0][K][2]][tu[0][K][3]][tu[0][K][4]] = i
#
#             K=K+1
#     if isinstance(tu[1], str):  # ('aa','bb')
#         Yaml[0] = tu[1]
#     print(Yaml)
#
# x = {'aa':{'bb':{'cc':{'ww':{'qq':''}}}},'dd':{'ee':{'ff':{'rr':{'ee':''}}}},'jj':{'hh':{'ii':{'zz':{'xx':''}}}}}
# jiexi(x,d)


# tup = ('x','s','se','ww')
# for tup_index in tup:
#     print(tup.index(tup_index))#这里不减一就会超出范围


# d = {'msg': '', 'code': '00', 'ok': True, 'body': {'feeTotal': '5600.00', 'feeInfo': {'offerRemark': None, 'offerId': None, 'feeId': '153836681959757626', 'offerName': None, 'feeName': '[国家开放大学]国家开放大学1001(1001)-202009-1000.00'}, 'feeList': [{'fdId': None, 'itemYear': '1', 'odId': None, 'itemType': '2', 'itemCode': 'Y1', 'discountType': None, 'orderNum': '2', 'feeId': None, 'payable': '1000.00', 'discount': '0.00', 'itemName': '代收第一年学费', 'amount': '1000.00', 'itemSeq': None}, {'fdId': None, 'itemYear': '1', 'odId': None, 'itemType': '4', 'itemCode': 'S1', 'discountType': None, 'orderNum': '3', 'feeId': None, 'payable': '250.00', 'discount': '0.00', 'itemName': '代收第一年书费', 'amount': '250.00', 'itemSeq': None}, {'fdId': None, 'itemYear': '1', 'odId': None, 'itemType': '5', 'itemCode': 'W1', 'discountType': None, 'orderNum': '4', 'feeId': None, 'payable': '150.00', 'discount': '0.00', 'itemName': '代收第一年网络费', 'amount': '150.00', 'itemSeq': None}, {'fdId': None, 'itemYear': '2', 'odId': None, 'itemType': '2', 'itemCode': 'Y2', 'discountType': None, 'orderNum': '5', 'feeId': None, 'payable': '1000.00', 'discount': '0.00', 'itemName': '代收第二年学费', 'amount': '1000.00', 'itemSeq': None}, {'fdId': None, 'itemYear': '2', 'odId': None, 'itemType': '4', 'itemCode': 'S2', 'discountType': None, 'orderNum': '6', 'feeId': None, 'payable': '250.00', 'discount': '0.00', 'itemName': '代收第二年书费', 'amount': '250.00', 'itemSeq': None}, {'fdId': None, 'itemYear': '2', 'odId': None, 'itemType': '5', 'itemCode': 'W2', 'discountType': None, 'orderNum': '7', 'feeId': None, 'payable': '150.00', 'discount': '0.00', 'itemName': '代收第二年网络费', 'amount': '150.00', 'itemSeq': None}, {'fdId': None, 'itemYear': '3', 'odId': None, 'itemType': '2', 'itemCode': 'Y3', 'discountType': None, 'orderNum': '8', 'feeId': None, 'payable': '1000.00', 'discount': '0.00', 'itemName': '代收第三年学费', 'amount': '1000.00', 'itemSeq': None}, {'fdId': None, 'itemYear': '3', 'odId': None, 'itemType': '4', 'itemCode': 'S3', 'discountType': None, 'orderNum': '9', 'feeId': None, 'payable': '250.00', 'discount': '0.00', 'itemName': '代收第三年书费', 'amount': '250.00', 'itemSeq': None}, {'fdId': None, 'itemYear': '3', 'odId': None, 'itemType': '5', 'itemCode': 'W3', 'discountType': None, 'orderNum': '10', 'feeId': None, 'payable': '150.00', 'discount': '0.00', 'itemName': '代收第三年网络费', 'amount': '150.00', 'itemSeq': None}, {'fdId': None, 'itemYear': '4', 'odId': None, 'itemType': '2', 'itemCode': 'Y4', 'discountType': None, 'orderNum': '11', 'feeId': None, 'payable': '1000.00', 'discount': '0.00', 'itemName': '代收第四年学费', 'amount': '1000.00', 'itemSeq': None}, {'fdId': None, 'itemYear': '4', 'odId': None, 'itemType': '4', 'itemCode': 'S4', 'discountType': None, 'orderNum': '12', 'feeId': None, 'payable': '250.00', 'discount': '0.00', 'itemName': '代收第四年书费', 'amount': '250.00', 'itemSeq': None}, {'fdId': None, 'itemYear': '4', 'odId': None, 'itemType': '5', 'itemCode': 'W4', 'discountType': None, 'orderNum': '13', 'feeId': None, 'payable': '150.00', 'discount': '0.00', 'itemName': '代收第四年网络费', 'amount': '150.00', 'itemSeq': None}, {'fdId': None, 'itemYear': '', 'odId': None, 'itemType': '3', 'itemCode': 'YS', 'discountType': None, 'orderNum': '100', 'feeId': None, 'payable': '0.00', 'discount': '0.00', 'itemName': '代收艺术加考费', 'amount': '0.00', 'itemSeq': None}]}}
#
#
# print(d['body']['feeInfo']['feeId'])


# d =(('1',),('2',),('3',),('4',),('5',),('6',),('7',),('8',),('9',),('10',),('11',),('12',),('13',),('14',),('15',),('16',))
#
# len(d)# = 16
# i = 0
# while(i<len(d)):
#     print(d[i:i+5])
#     i=i+5
#
#
# print(d[0:19])






