# food order app

price_pizza = 70.50  # U.C
price_salad = 20.00  # U.C
price_soup  = 15.00  # U.C

q_pizza = int(input("how many pizzas?"))
q_salad = int(input("how many salads?"))
q_soup  = int(input("how many soups?"))

cost = price_pizza*q_pizza+\
       price_salad*q_salad+\
       price_soup*q_soup  

print("----------------------------")

print("####### RESTAURANT MENU #######") 
print("1. Pizza = 70.50  U.C")
print("2. Salad = 20.00  U.C")
print("3. Soup  = 15.00  U.C")

print("----------------------------")

print("Pizza: ",q_pizza,"pizzas")
print("Salad: ",q_salad,"salads")
print("Soup:  "  ,q_soup,"soups")

print("----------------------------")

print("Pizza: ",q_pizza * price_pizza ,"U.C")
print("Salad: ",q_salad * price_salad,"U.C")
print("Soup:  "  ,q_soup * price_soup,"U.C")

print("----------------------------")

print("TOTAL COST: ", cost, "U.C")