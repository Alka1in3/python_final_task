# Список покупок
purchases = [
 {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
 {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
 {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
 {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

# Общая вырчка
def total_revenue(purchases):
    revenue = 0
    for purchase in purchases:
        revenue += purchase["price"] * purchase["quantity"]
    return revenue

# Число уникальных товаров по категориям
def items_by_category(purchases):
    categories = dict()
    for purchase in purchases:
        if purchase["category"] not in categories:
            categories[purchase["category"]] = []
            categories[purchase["category"]].append(purchase["item"])
        else:
            categories[purchase["category"]].append(purchase["item"])
    return categories

# Покупки дороже min_price
def expensive_purchases(purchases, min_price):
    expensive_purchases = []
    for purchase in purchases:
        if purchase["price"] > min_price:
            expensive_purchases.append(purchase)
    return expensive_purchases

# Средняя цена товаров в категории
def average_price_by_category(purchases):
    categories = dict()
    for purchase in purchases:
        if purchase["category"] not in categories:
            categories[purchase["category"]] = []
            categories[purchase["category"]].append(purchase["price"])
        else:
            categories[purchase["category"]].append(purchase["price"])
    for category in categories:
        categories[category] = sum(categories[category]) / len(categories[category])
    return categories

# Самая популярная категория
def most_frequent_category(purchases):
    categories = dict()
    for purchase in purchases:
        categories[purchase["category"]] = categories.get(purchase["category"], 0) + purchase["quantity"]

    return max(categories, key=categories.get)

min_price = 1.0

print(f'Общая выручка: {total_revenue(purchases)}\n'
      f'Товары по категориям: {items_by_category(purchases)}\n'
      f'Покупки дороже {min_price}: {expensive_purchases(purchases, min_price)}\n'
      f'Средняя цена по категориям: {average_price_by_category(purchases)}\n'
      f'Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}')
