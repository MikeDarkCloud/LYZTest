import re
def regx(context,patt):
    pattern = re.compile(patt)
    result = re.findall(pattern, context, flags=0)
    return result






