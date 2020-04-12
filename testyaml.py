import yaml
from public.YamlParser import *
def ryaml():
    with open('C:\YZeducation\PyProject\LYZTest\test_data\pay.yaml', 'r', encoding='utf-8') as f:
        return yaml.load(f)


def wyaml(content):
    with open('F:\\Github\\LYZTest\\test_data\\test.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(content, f, default_flow_style=False, encoding='utf-8', allow_unicode=True)




# di = {'ds':{'dh':"dtet"}}
#
# YamlParser('test').setYaml(di)

d = {'name':'孙悟空','age':18,'gender':'男'}

# 通过遍历keys()来获取所有的键
for k in d.keys() :
  print(k , d[k])