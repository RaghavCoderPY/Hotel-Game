print("Welcome to my Hotel!")


# function for checking budget
def check_budget(budget, price, food):
    if price == budget:
        print("Take %s", food)
    elif price < budget:
        print(f"Ok you buy and I give you ₹{budget - price}")
    else:
        print("Do not take food")


# dict of food item price
price = {
    "tomato potato": 320,
    "potato": 100,
    "pumpkin Pie": 560,
    "mutter paneer": 999,
    "shahi paneer": 899,
    "chicken": 7999
}
# list of foods
a = 0
for food, prices in price.items():
    a = a + 1
    print(f"{a}. The price of {food.capitalize()} Rice/Roti is ₹{prices}")
    if food == "Pumpkin Pie":
        print(f"{a}. The price of {food} is ₹{prices}")
        continue
else:
    print('food list ends')

# Ordering Food
user = input("Enter food: ").lower()
budget = int(input("Enter your budget: "))
check_budget(budget, price.get(user), user)
