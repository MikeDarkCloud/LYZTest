import re


def regx(context,patt):
    #pattern = re.compile(r'(?<=(?:<input type="hidden" name="_web_token" value="))[1-9]\d*(?=(?:" />))')
    pattern = re.compile(patt)
    return re.findall(pattern, context, flags=0)


print(regx('*ture*','fqerqwrqwrqture'))