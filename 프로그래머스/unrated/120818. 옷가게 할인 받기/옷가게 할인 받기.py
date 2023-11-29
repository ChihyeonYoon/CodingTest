def solution(price):
    if price < 100000:
        return price
    if price >=100000 and price < 300000:
        return int(price*0.95)
    if price >=300000 and price < 500000 :
        return int(price*0.9)
    if price >=500000:
        return int(price*0.8)
    