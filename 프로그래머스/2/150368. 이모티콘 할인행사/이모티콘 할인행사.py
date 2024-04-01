def solution(users, emoticons):
    answer = []
    
    from itertools import product

    # 주어진 리스트
    values = [10, 20, 30, 40]

    # 리스트의 길이
    length = len(emoticons)  # 원하는 리스트의 길이를 지정합니다.

    # 각 원소로 갖는 일정 길이의 리스트의 모든 조합을 담고 있는 리스트 생성
    discounts = list(product(values, repeat=length))

    result_emoticon_plus, result_selling  = 0,0
    for discount in discounts:
        emoticon_plus = 0
        selling = 0
        discounted_prices = []

        for idx in range(len(discount)):
            discounted_prices.append([discount[idx],(100-discount[idx]) * emoticons[idx] // 100]) # [discount_rate, discounted_price]

        # discounted_prices.sort(key=lambda x:x[1])

        for user in users:
            user_dis, user_money = user[0], user[1]
            purchase = 0

            for dis in discounted_prices:
                if user_dis <= dis[0]:
                    selling += dis[1]
                    purchase += dis[1]
                    # user_money -= dis[1]

            if user_money <= purchase:
                emoticon_plus +=1
                selling -= purchase

        # print(emoticon_plus, selling)

        if result_emoticon_plus < emoticon_plus :
            result_emoticon_plus, result_selling = emoticon_plus, selling
        elif result_emoticon_plus == emoticon_plus:
            if result_selling <= selling:
                result_selling = selling
    
    # print(result_emoticon_plus, result_selling)
            
    return [result_emoticon_plus, result_selling]