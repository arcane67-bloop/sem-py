a = input().split()

for i in range(len(a)):
	a[i] = int(a[i])

def is_positive(num :int) -> bool:
	if num >= 0:
		return True
	else:
		return False

def count_positive(a: list) -> int:
	count = 0
	for obj in a:
		if is_positive(obj) == True:
			count += 1
	return count

def count_negative(a: list) -> int:
	count_n = 0
	for obj_n in a:
		if is_positive(obj_n) == False:
			count_n += 1
	return count_n

print(count_positive(a))
print(count_negative(a))

