# 4. Write a program which accepts one number and prints that many numbers starting from 1.

# Input : 5
# Output : 1  2   3   4   5

def Display(No):
    for i in range(1, No+1):
        print(i, end="\t")
        
def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()