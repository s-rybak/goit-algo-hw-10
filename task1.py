import pulp

model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

lymonade = pulp.LpVariable("lymonade", lowBound=0, cat="Integer")
fruit_juice = pulp.LpVariable("juice", lowBound=0, cat="Integer")

model += lymonade + fruit_juice, "Count of drinks"

model += 2 * lymonade + 1 * fruit_juice <= 100, "Water"
model += 1 * lymonade <= 50, "Sugar"
model += 1 * lymonade <= 30, "Lemon juice"
model += 2 * fruit_juice <= 40, "Fruit juice"


model.solve()

print("Кількість лимонаду:", lymonade.varValue)
print("Кількість фруктового соку:", fruit_juice.varValue)
