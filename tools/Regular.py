import re
def regx(context,patt):
    pattern = re.compile(patt)
    result = re.findall(pattern, context, flags=0)
    return result



def regxChang(context,rex0,rex1):
    return context.replace(rex0,rex1)




# d = '[{''odId'': None, ''fdId'': None, ''payable'': ''1000.00'', ''amount'':''1000.00'', ''discountType'': None,'
# print(regxChang(d,'None','null'))
