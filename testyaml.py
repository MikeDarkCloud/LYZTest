import yaml

d = ((('aa', 'bb', 'cc','ww','qq'), ('dd', 'ee', 'ff','rr','ee'), ('jj', 'hh', 'ii','zz','xx')), ([1234], '13', '14'))


# d[0] = ,xx(('aa','bb','cc'),('dd','ee','ff'),('jj','hh','ii'))

def jiexi(Yaml, tu: tuple):
    K=0
    if len(tu[0]) != len(tu[1]):
        raise Exception ("参数错误！")
    if isinstance(tu[0], tuple):  # (('aa','bb','cc'),('dd','ee','ff'),('jj','hh','ii'))
        for i in tu[1]:
            # 取出一个d[0][0]('aa','bb','cc')
            if isinstance(tu[0][K], tuple):  # ('aa','bb','cc')
                if len(tu[0][K]) == 1:
                    Yaml[tu[0][K][0]] = i

                if len(tu[0][K]) == 2:
                    Yaml[tu[0][K][0]][tu[0][K][1]] = i

                if len(tu[0][K]) == 3:
                    Yaml[tu[0][K][0]][tu[0][K][1]][tu[0][K][2]] = i

                if len(tu[0][K]) == 4:
                    Yaml[tu[0][K][0]][tu[0][K][1]][tu[0][K][2]][tu[0][K][3]] = i

                if len(tu[0][K]) == 5:
                    Yaml[tu[0][K][0]][tu[0][K][1]][tu[0][K][2]][tu[0][K][3]][tu[0][K][4]] = i

            K=K+1
    if isinstance(tu[1], str):  # ('aa','bb')
        Yaml[0] = tu[1]
    print(Yaml)

x = {'aa':{'bb':{'cc':{'ww':{'qq':''}}}},'dd':{'ee':{'ff':{'rr':{'ee':''}}}},'jj':{'hh':{'ii':{'zz':{'xx':''}}}}}
jiexi(x,d)