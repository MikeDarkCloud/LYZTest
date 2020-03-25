import unittest
import ddt

def add(a,b):
    res=a+b
    return res

#声明要使用ddt
@ddt.ddt
class MyTest(unittest.TestCase):
    #初始化
    def setUp(self):
        print('setup')

    #ddt.data中添加测试数据
    # @ddt.data([1,2,3],[2,3,5])
    @ddt.file_data('testdata.yaml')
    @ddt.unpack
    def test_add(self,value):
        print(value)
        a=value[0]
        b=value[1]
        res=add(a,b)
        self.assertEqual(res,e)
    #结束
    def tearDown(self):
        print('tearDown')

if __name__ == '__main__':
    unittest.main()