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

if __name__ == '__main__':
    initial_location = os.getcwd()

    # 1. CREATING A FOLDER. PUT THE EXACT DIRECTORY WITH FOLDER NAME
    # CALL THE METHOD folder(): folder(file_location)
    crt_fld = CreateFolder()
    crt_fld.folder("location of the directory. e.g: C:/Users/Md Redwanuzzaman/Desktop/Test Folder")

    # 2. CREATING A FILE. PUT THE EXACT DIRECTORY WITH FILE NAME
    # CALL THE METHOD create_file(): create_file(file location)
    crt_fl = CreateFile()
    crt_fl.create_file("location of the directory")

    # 3. ADDING A DIRECTORY TO ANOTHER DIRECTORY.
    # CALL THE METHOD (add()): add(source location, destination location)
    add_dir = AddDirectory()
    add_dir.add("source", "destination")
    
    # 4. WRITING A STRING CONTENT TO A FILE.
    # CALL THE METHOD write(): write(file_location, content)
    wf = WriteFile()
    wf.write("location of the file to write", "content to write")

    # 5. READ STRING CONTENT FROM FILE
    # CALL THE METHOD read(): read(file_location)
    rf = ReadFile()
    rf.read("location of the file to read")

    # 6. CLEAR THE CONTENT OF A FILE
    # CALL THE METHOD clear(): clear(file_location)
    clr_fl = ClearFile()
    clr_fl.clear("location of the file to clear")

    # 7. GET THE SIZE OF THE CONTENT OF A FILE
    # CALL THE METHOD get_length(): get_length(file_location)
    # THE METHOD RETURNS THE LENGTH. STORE IT IN A VARIABLE OR CALL THE get_length() IN print() BUILT IN METHOD
    c_len = ContentLength()
    c_len.get_length("location of the file")

    # 8. GET THE SIZE OF THE CONTENT OF A FOLDER
    # CALL THE METHOD folder_size(): folder_size(folder_location)
    fld_sz = FolderSize()
    fld_sz.folder_size("location of the folder")

    # 9. PRINT THE FILE/FOLDER NAMES INSIDE A FOLDER
    # CALL THE METHOD file_list(): file_list(folder_location)
    fld_fls = FolderFiles()
    fld_fls.file_list("location of the folder")

    # 10. WALK TREE OF A FOLDER
    # CALL THE METHOD tree(): tree(location of the folder)
    wt = WalkTree()
    wt.tree("location of the folder")
