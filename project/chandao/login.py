

def login(dirver,usr,psw):
    dirver.input('id','account',usr)
    dirver.input('name','password',psw)
    dirver.click('id','submit')
