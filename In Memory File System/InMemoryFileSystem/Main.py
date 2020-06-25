import os
import logging
logging.basicConfig(filename="logName.txt", level=logging.DEBUG)
from Features import Features
from FileSystem import FileSystem

if __name__ == '__main__':

    print("*" * 35)
    print("   WELCOME TO MEMORY FILE SYSTEM")
    print("*" * 35 + "\n\n")

    print("You're Currently In This Directory: {}\n".format(os.getcwd()))
    change_directory = input("Would You Like To Change Your Directory ? (Yes/No)\n")
    if change_directory.lower() in ['yes', 'y']:
        new_directory = input("Enter New Directory (A Complete Memory Location): ")
        try:
            os.chdir(new_directory)
            print("\nNow You're In: {}\n".format(os.getcwd()))
        except Exception as e:
            print("Not a Valid Directory")
            print(e)
    feature = Features()
    feature.feature_list()
    fs = FileSystem()
    fs.file_system()
