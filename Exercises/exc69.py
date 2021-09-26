a = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
x = int(input("Type a number between zero and twenty, and I'll show it written in cursive:"))
while x > 20 or x < 0:
    x = int(input("Sory, you typed something wrong. Type a number between zero and twenty, and I'll show it written in cursive:"))
print(a[x])
