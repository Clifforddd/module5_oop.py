from module5_mod import NumberStore

def main():
    store = NumberStore()

    N = int(input("Enter the number of numbers (N): "))

    for i in range(N):
        num = int(input(f"Enter number {i+1} of {N}: "))
        store.add_number(num)

    X = int(input("Enter the number to find (X): "))
    index = store.find_number(X)

    print(f"Index of the number: {index}")

if __name__ == "__main__":
    main()
