import csv
import os

def create_sample_files():
    file_path = os.path.join(os.path.dirname(__file__), "Book1(Recovered).csv")
    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Item', 'Stock', 'Price'])
            writer.writerow(['Laptop', 50, 1000])
            writer.writerow(['Smartphone', 100, 500])

class Owner:
    def __init__(self):
        create_sample_files()

    def read_file(self):
        file_path = os.path.join(os.path.dirname(__file__), "Book1(Recovered).csv")
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def create_file(self, data):
        file_path = os.path.join(os.path.dirname(__file__), "Book1(Recovered).csv")
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)

    def update_file(self, row_index, updated_data):
        file_path = os.path.join(os.path.dirname(__file__), "Book1(Recovered).csv")
        rows = []
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        if row_index < len(rows):
            rows[row_index] = updated_data

        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    def delete_row(self, row_index):
        file_path = os.path.join(os.path.dirname(__file__), "Book1(Recovered).csv")
        rows = []
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        if row_index < len(rows):
            rows.pop(row_index)

        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

def main():
    owner = Owner()
    while True:
        print("\nOptions:")
        print("1. View file")
        print("2. create")
        print("3. Update ")
        print("4. Delete")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nViewing file:")
            owner.read_file()
        elif choice == "2":
            item = input("Enter item name: ")
            stock = input("Enter stock quantity: ")
            price = input("Enter price: ")
            owner.create_file([item, stock, price])
            print("item added successfully.")
        elif choice == "3":
            row_index = int(input("Enter the row index to update (starting from 0): "))
            item = input("Enter new item name: ")
            stock = input("Enter new stock quantity: ")
            price = input("Enter new price: ")
            owner.update_file(row_index, [item, stock, price])
            print(" updated successfully.")
        elif choice == "4":
            row_index = int(input("Enter the row index to delete (starting from 0): "))
            owner.delete_row(row_index)
            print("Row deleted successfully.")
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
