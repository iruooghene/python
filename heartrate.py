age = int(input("Enter age: "))
training_intensity=float(input("Enter training_intensity: "))
resting_heart_rate=int(input("Enter resting_heart_rate: "))
m= training_intensity / 100

print("training intensity: ", m)
heart_rate_reserve= (220 - age) - resting_heart_rate
print("heart rate reserve is:", heart_rate_reserve)
target_heart_rate= heart_rate_reserve * m + resting_heart_rate

print("target heart rate is:", target_heart_rate)