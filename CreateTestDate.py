from common.base import *
from common.conf import *
from tools.CreateIdentity import *
from tools.CreateMobile import *
class createTestdate():
    '''生成测试数据'''
    def createRegiesterTestdate(self):

        id_card = create_identity(int(area_dict1), 22, 1)
        mobile = get_mobile()
        y = Config()
        t = y.Ryaml()
        t['data']['idCard'] = id_card
        t['data']['idCard'] = mobile
        y.Wyaml(t)
        h=y.Hyaml()
        print(h['hearder'])
        r = YzApi()
        print(t['data'])
        qq=r.lapi(method= 'post',urls='http://bms.yzwill.cn/recruit/recruitAdd.do',data=t['data'],headers=h['hearder'])
        print(qq.text)
if __name__ == '__main__':
    q=createTestdate()
    r = q.createRegiesterTestdate()
