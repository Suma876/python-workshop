
storage = []

n = int(input("Enter the number of items: "))
        
for i in range(n):
	item = input(f"Enter item {i + 1}: ")
	storage.append(item)

print("List of items:", storage)

brought = input("Customer brought: ")

if brought in storage:
	storage.remove(brought)
	print("Item purchased successfully.")
else:
	print("Item not available.")

print("List after purchase:", storage)