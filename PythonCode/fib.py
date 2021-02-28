fib = [1,1]
current = 0
times = int(input("Numbers to calculate in the Fibonacci sequence: "))
dump = False
dumpq = input("Dump results to file afterwards? ")
if dumpq.lower() in ["y","yes","ok"]:
	dump = True
elif dumpq.lower() in ["n","no"]: pass
else: print("Invalid answer. Will treat as 'no' instead.")

for i in range(2,times+1):
	if len(fib) > 100:
		fib.pop(0)
		current = fib[97] + fib[98]
	else:
		current = fib[i-2] + fib[i-1]
	fib.append( current )

print("Press ENTER to see the last 100 numbers from the Fibonacci sequence. ")
input()
for x in fib:
	print(x)

if dump:
	print("Dumping to file...")
	file = open("Program Files/fib.txt","wt")
	file.writelines(str(fib))
	print("Done! You can view it as 'fib.txt' in the 'Program Files' subfolder of the current folder2")
	file.close()