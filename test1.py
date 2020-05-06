import requests


url = 'http://test.yzwill.cn:8180/proxy/us/usPosting/1.0/'
data = {'scTitle':'','scText':'','scPicUrl':'','scVideoUrl':'','scType':'','nickName':'',
        'realNam':'','unvsName':'','pfsnName':'','stdName':'','learnId':'','mobile':'',
        'grade':'','unvsId':'','pfsnId':'','recruitType':'','scAddress':'','addressName':'',
        'gisLongitude':'','gisLatitude':'','aiteUserId':'','htIds':'','htNames':''}
r = requests.post(url= url,data = data)

print(r.text)