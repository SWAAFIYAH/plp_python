price = int(input("please enter original price:" ))
discount_percent = int(input("please enter percentage discount:" ))



def calculate_discount(price, discount_percent):

    if discount_percent >= 20 :
     discount = (discount_percent / 100) * price
     final_price = price - discount

    else:
        final_price = price
    return final_price  

   

final_price = calculate_discount(price, discount_percent)
print(final_price)





