import time
print("Fortune teller ver. 0.9.2")
print('-------------------------')
print()
x = input("Please enter your name: ")
animation = ["", ".", "..", "...", "....", "....."]
id = 0
compute = "Computing"
for i in range(6):
    print(compute + animation[id % len(animation)], end="\r")
    id += 1
    time.sleep(0.5)
print(f"Hello {x}. You are gay.")