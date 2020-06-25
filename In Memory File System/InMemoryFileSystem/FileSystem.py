import os
from CreateFolder import CreateFolder
from AddDirectory import AddDirectory
from FolderFiles import FolderFiles
from FolderSize import FolderSize
from WalkTree import WalkTree
from CreateFile import CreateFile
from ReadFile import ReadFile
from WriteFile import WriteFile
from ClearFile import ClearFile
from ContentLength import ContentLength
from Features import Features

folder_location = {}
file_location = {}


class FileSystem:

    def file_system(self):
        while True:
            # Features.feature_list(self)
            choice = input("\nChoose Your Option: ")
            if choice == '1':
                folder_name = input("\nEnter The Folder Name: ")
                folder_address = os.path.join(os.getcwd(), folder_name)
                CreateFolder.folder(self, folder_address)
                folder_location[folder_name] = folder_address
            elif choice == '2':
                file_name = input("\nEnter The File Name: ")
                file_address = os.path.join(os.getcwd(), file_name)
                CreateFile.create_file(self, file_address)
                file_location[file_name] = file_address
            elif choice == '3':
                while True:
                    print("Where You Want To Move?")
                    print("(1) File To Folder")
                    print("(2) Folder To Folder")
                    move = input("\nEnter Your Choice: ")
                    if move == '1':
                        source = input("\nEnter The Source File Name: ")
                        source_address = file_location[source]
                        destination = input("\nEnter The Destination Folder Name: ")
                        destination_address = folder_location[destination]
                        AddDirectory.add(self, source_address, destination_address)
                        file_location[source] = os.path.join(destination_address, source)
                        break
                    elif move == '2':
                        source = input("\nEnter The Source Folder Name: ")
                        source_address = folder_location[source]
                        destination = input("Enter The Destination Folder Name: ")
                        destination_address = folder_location[destination]
                        AddDirectory.add(self, source_address, destination_address)
                        folder_location[source] = os.path.join(destination_address, source)
                        break
                    else:
                        print("Invalid Input, Type 1 or 2")
            elif choice == '4':
                while True:
                    print("(1) Write in a New File")
                    print("(2) Write in an Existing File")
                    write_choice = input("\nChoose Your Option: ")
                    if write_choice == '1':
                        file = input("Enter The File Name: ")
                        file_address = os.path.join(os.getcwd(), file)
                        content = input("\nEnter The Content You Want To Write: ")
                        WriteFile.write(self, file_address, content)
                        file_location[file] = file_address
                        break
                    elif write_choice == '2':
                        file = input("\nEnter The File Name: ")
                        file_address = file_location[file]
                        content = input("\nEnter The Content You Want To Write: ")
                        WriteFile.write(self, file_address, content)
                        break
                    else:
                        print("Invalid Input, Type 1 or 2")
            elif choice == '5':
                file = input("\nEnter The File Name: ")
                file_address = file_location[file]
                ReadFile.read(self, file_address)
            elif choice == '6':
                file = input("\nEnter File Name: ")
                file_address = file_location[file]
                ClearFile.clear(self, file_address)
            elif choice == '7':
                file = input("\nEnter File Name: ")
                file_address = file_location[file]
                ContentLength.get_length(self, file_address)
            elif choice == '8':
                folder = input("\nEnter Folder Name: ")
                folder_address = folder_location[folder]
                FolderSize.folder_size(self, folder_address)
            elif choice == '9':
                required_folder = input("\nEnter Folder Name: ")
                FolderFiles.file_list(self, folder_location[required_folder])
            elif choice == '10':
                folder = input("\nEnter Folder Name: ")
                WalkTree.tree(self, folder_location[folder])
            elif choice == '11':
                print(os.getcwd())
            elif choice == '12':
                FolderFiles.file_list(self, os.getcwd())
            elif choice == '13':
                print("\nGood Bye. See you Soon")
                exit()
            else:
                print("\nInvalid Choice")


# f = FileSystem()
# f.file_system()
