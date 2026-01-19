# 1. Write a program which accepts one character and checks whether it is vowel or consonant

# Input : a
# Output : Vowel

def ChkAlphabet(ch):
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or
        ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'
       ):
        return True
    else:
        return False

def main():
    Character = ''
    Ret = False

    print("Enter the character : ")
    Character = input()

    Ret = ChkAlphabet(Character)

    if(Ret == True):
        print("It is Vowel")
    else:
        print("It is Consonant")

if __name__ == "__main__":
    main()