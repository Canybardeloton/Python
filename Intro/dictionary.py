fruits = {
	"apple" : "red",
	"banana" : "yellow",
	"orange" : "orange"
}
print(fruits)

fruits["kiwi"] = "green"
print(fruits)

banan_color = fruits["banana"]
print(banan_color)

fruits["apple"] = "green"
print(fruits["apple"])

del fruits["orange"]
print(fruits)