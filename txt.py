from utils.BasicPage import Basic

dr = Basic()
dr.open('https://blog.csdn.net/skullfang/article/details/78820541')
print(dr.text('xpath','//*[@id="mainBox"]/main/div[1]/div[1]/div/div[1]/h1'))