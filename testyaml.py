import yaml

def ryaml():
    with open('C:\YZeducation\PyProject\LYZTest\test_data\pay.yaml', 'r', encoding='utf-8') as f:
        return yaml.load(f)


def wyaml(content):
    with open('C:\YZeducation\PyProject\LYZTest\test_data\pay.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(content, f, default_flow_style=False, encoding='utf-8', allow_unicode=True)


print(ryaml())