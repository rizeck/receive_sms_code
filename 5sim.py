from fivesim import FiveSim
import requests
import time

print('↓↓以下にAPIキーをペースト↓↓')
Key = input()

API_KEY = Key

client = FiveSim(API_KEY) 

price = client.price_requests_by_country_and_product(country='vietnam' ,product='twitter')

#print(price)
#print(price['russia'])
info_pr = str(price)
target = 'cost'
idx = info_pr.find(target)
r = info_pr[idx+len(target)+3:]  


target2 = "count"

idx2 = r.find(target2)
x = r[:idx2]
pr = x[:-3]
ex = "現在のSMS認証の値段は"
ex2 = '₽(ルーブル)です。'
print(ex+pr+ex2)
bn = input("購入する場合は「buy」と入力しEnter：")

if bn == 'buy':
	

#ここで電話番号購入
    num = client.buy_number(country='vietnam', operator='any', product='twitter')
#ここから電話番号の抽出
    numstr = str(num)
    target = 'phone'
    idx = numstr.find(target)
    r =  numstr[idx+len(target)+4:]  


    target2 = "operator"

    idx2 = r.find(target2)
    x = r[:idx2]
#電話番号確定
    number = x[:-4]

    print(number)

#ここから注文idの抽出
    numstr = str(num)
    target = 'id'
    idx = numstr.find(target)
    r =  numstr[idx+len(target)+3:]  


    target2 = "phone"

    idx2 = r.find(target2)
    x = r[:idx2]
    
    idnum = x[:-3]
    print('sms送信後「send」と入力しEnter')
    print('キャンセルの場合は「cancel」と入力しEnter')
    string = input()
    if string == "send":
        sms = client.check_order(order_id=idnum)
    #print(str(sms))
    #ここから注文smsの抽出
        smsstr = str(sms)
    
    #print(str(sms))
        target = 'text'
        idx = smsstr.find(target)
        r =  smsstr[idx+len(target)+3:]  


        target2 = "code"

        idx2 = r.find(target2)
        x = r[:idx2]
    #sms確定
        code = x[:-3]
        if "'sms': []," in str(sms):
            print("まだ取得出来ていません")
        
        else:
            print(code)
    if string == 'cancel':
    	client.cancel_order(order_id=idnum)



