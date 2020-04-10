import yaml

def ryaml():
    with open('C:\YZeducation\PyProject\LYZTest\test_data\pay.yaml', 'r', encoding='utf-8') as f:
        return yaml.load(f)


def wyaml(content):
    with open('C:\YZeducation\PyProject\LYZTest\test_data\pay.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(content, f, default_flow_style=False, encoding='utf-8', allow_unicode=True)


def rr(*dd):
    print(dd[0])
    print(dd[1])

rr('2222',3333)
