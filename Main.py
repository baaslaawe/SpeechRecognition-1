from AudioManager import *

if __name__ == '__main__':
    auto_treshold()
    while 1:
        print("Select an option:")
        option = input("\t1) Learn\n\t2) Search\n\t3) Exit\nCommand: ")

        if option == "1":
            record_to_file()
        elif option == "2":
            break
        else:
            break
    print("Program exited successfully")
