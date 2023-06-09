compare = int(input("nhập số ngày trong tuần: "))
if compare not in [0, 1 , 2 , 3 , 4 , 5 , 6 ]: print("input error, try again"); exit()
#if compare < 1 and compare > 7: print("input errand, try again"); exit()
elif compare == 1: day_of_week = "monday"
elif compare == 2: day_of_week = "tuesday"
elif compare == 3: day_of_week = "wednesday"
elif compare == 4: day_of_week = "thursday"
elif compare == 5: day_of_week = "friday"
elif compare == 6: day_of_week = "saturday"
else: day_of_week = "sunday"

print(day_of_week)