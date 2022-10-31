weight = 41.5
ground_cost = ""
p_ground_cost = 125
drone_cost = ""

print("Ground Shipping")
if weight <= 2:
  ground_cost = 1.50 * weight + 20
elif weight > 2 and weight <= 6:
  ground_cost = 3 * weight + 20
elif weight > 6 and weight <= 10:
  ground_cost = 4 * weight + 20
else:
  ground_cost = 4.75 * weight + 20

print(ground_cost)

print("Premium Ground Shipping")

print(p_ground_cost)

print("Drone Shipping")
if weight <= 2:
  drone_cost = 4.50 * weight
elif weight > 2 and weight <= 6:
  drone_cost = 9 * weight
elif weight > 6 and weight <= 10:
  drone_cost = 12 * weight
else:
  drone_cost = 14 * weight

print(drone_cost)
