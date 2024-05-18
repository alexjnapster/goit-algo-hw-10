import pulp

# Створюємо модель лінійного програмування
model = pulp.LpProblem("Оптимізація виробництва напоїв", pulp.LpMaximize)

# Змінні рішення
lemonade = pulp.LpVariable('Лимонад', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('Фруктовий сік', lowBound=0, cat='Continuous')

# Функція цілі: максимізація загальної кількості вироблених продуктів
model += lemonade + fruit_juice, "Загальна кількість напоїв"

# Обмеження на ресурси
model += 2 * lemonade + 1 * fruit_juice <= 100, "Обмеження на воду"
model += 1 * lemonade <= 50, "Обмеження на цукор"
model += 1 * lemonade <= 30, "Обмеження на лимонний сік"
model += 2 * fruit_juice <= 40, "Обмеження на фруктове пюре"

# Розв'язуємо модель
model.solve()

# Виводимо результати
print("Статус:", pulp.LpStatus[model.status])
print("Кількість виробленого Лимонаду:", pulp.value(lemonade))
print("Кількість виробленого Фруктового соку:", pulp.value(fruit_juice))