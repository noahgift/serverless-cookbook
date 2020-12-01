import json

def hello_world(request):
 
    request_json = request.get_json()
    print(f"This is my payload: {request_json}")
    if request_json and 'amount' in request_json:
        raw_amount = request_json['amount']
        print(f"This is my amount: {raw_amount}")
        amount = float(raw_amount)
        print(f"This is my float amount: {amount}")
    res = []
    coins = [1,5,10,25]
    coin_lookup = {25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}
    coin = coins.pop()
    num, rem  = divmod(int(amount*100), coin)
    res.append({num:coin_lookup[coin]})
    while rem > 0:
        coin = coins.pop()
        num, rem = divmod(rem, coin)
        if num:
            if coin in coin_lookup:
                res.append({num:coin_lookup[coin]})
    result = f"This is the res: {res}"
    return result
