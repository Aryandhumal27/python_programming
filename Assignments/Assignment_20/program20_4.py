# 4. Design a Python application that creates three threads named Small, Capital, and Digits.

# -> All threads should accept a string as input.
# -> The Small thread should count and display the number of lowercase characters.
# -> The Capital thread should count and display the number of uppercase characters.
# -> The Digits thread should count and display the number of numeric digits.
# -> Each thread must also display:
#    -> Thread ID
#    -> Thread Name 

import threading

def ChkLowerCase(String):
    LowerCount = 0
    for i in String:
        if(i >= 'a' and i <= 'z'):
            LowerCount = LowerCount + 1

    print("Number of Lower Case Characters are : ", LowerCount)
    print("Thread ID : ", threading.get_ident())
    print("Thread Name : ", threading.current_thread().name)

def ChkUpperCase(String):
    UpperCount = 0
    for i in String:
        if(i >= 'A' and i <= 'Z'):
            UpperCount = UpperCount + 1

    print("Number of Upper Case Characters are : ", UpperCount)
    print("Thread ID : ", threading.get_ident())
    print("Thread Name : ", threading.current_thread().name)

def NumericDigit(String):
    NumericCount = 0
    for i in String:
        if(i >= '0' and i <= '9'):
            NumericCount = NumericCount + 1

    print("Number of numeric digits are : ", NumericCount)
    print("Thread ID : ", threading.get_ident())
    print("Thread Name : ", threading.current_thread().name)

def main():
    String = input("Enter the string : ")

    t1 = threading.Thread(target=ChkLowerCase, args=(String, ), name="Small")
    t2 = threading.Thread(target=ChkUpperCase, args=(String, ), name="Capital")
    t3 = threading.Thread(target=NumericDigit, args=(String, ), name="Digit")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("End of main")

if __name__ == "__main__":
    main()
