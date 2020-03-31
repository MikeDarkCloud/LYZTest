import base64

class YBase64:

    def base64code(self,text):
        datas = base64.b64encode(text).decode('utf-8')
        return datas