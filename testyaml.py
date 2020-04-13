import yaml

class T():
    def read(self):
        with open('C:\\YZeducation\\PyProject\LYZTest\\test_data\\test.yaml', 'r', encoding='utf-8') as f:

            return yaml.load(f)



class Y():
    def test(self):
        T().read()




a = ('ds','dd')
b = 'ds'

d= T().read().get(a[0])
f= T().read().get(b)
k= T().read().get('ds')
print(d)
print(f)
print(k)
print(T().read())
