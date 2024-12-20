user_input = input("Enter a list of interger separated by commas : ")
list = user_input.split(",")
i = 0
result = 0
average = 0

print(f"user_input : {user_input}")
print(f"list : {list}")

for x in list :
	list[i] = int(list[i])
	i = i + 1

i = 0
for num in list :
	result += list[i]
	i = i + 1
print(f"result : {result}")

count = 0
for x in list :
	count += 1

average = result / count
print(f"average : {average}")

count = 0
i = 0
for y in list :
	if list[i] > average :
		count += 1
	i += 1
print(f"count : {count}")

count = 0
i = 0
j = 0
for i in range(len(list)) :
	for j in range(i + 1, len(list)) :
		if (list[i] == list[j]) :
			count += 1

print(f"count : {count}")