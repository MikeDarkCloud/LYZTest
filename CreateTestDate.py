from common.base import *
from common.conf import *
from tools.CreateIdentity import *
from tools.CreateMobile import *
def createTestdate(num = 10):

    while(num):
        id_number = create_identity(int(area_dict1), 22, 1)
        mobile = create_mobile()
        Config().Wyaml('regiester','')
        YzApi().lapi()
