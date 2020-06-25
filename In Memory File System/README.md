## In-Memory-File-System


Software Requirements: 
***************************** 
1. Python 3 [ To run the Program] 
2. A Python IDE (e.g: Pycharm, Atom, VSCode) [ To Browse the Codes ]  


Features: 
************************* 
1. Create A Folder 
2. Create A File 
3. Add A File To A Folder 
3. Add A Folder To A Folder 
4. Write A String Content To A File 
5. Read String Content From File 
6. Clear The Content Of The File 
7. Get The Size Of The Content Of The File 
8. Get The Size Of The Content Of A Folder 
9. Print The File/folder Names Inside A Folder 
10. Walk The Tree Of A Folder Including All Of Its Subfolders 
11. Watch Current Directory   
12. Watch Current Directory Files


How To Run: 
******************************* 
1. Unzip The Folder "InMemoryFileSystem" 
2. Load All The Classes in the folder Or Run the folder in "Open As A Project" in the IDE. 
3. Go To The Main.py To Run  


User Manual: 
********************************* 
>> Initially The Program will show you in which directory you're now. Then You can change the directoy by typing ("Yes" or "No")
>> To Change the Directory give An Exact memory location (e.g: C:\Users\Md Redwanuzzaman\Desktop ) 
1. For Creating A Folder: Choose Option 1. Then Write The Folder Name: (e.g: Test Folder)  
2. For Creating A File: name the file. [use the file extension (e.g: file.txt)]  
3. For Adding A Directory To Another Directory:  add(source location, destination location) 
4. For Writing A String Content To A File. Cgive the file name and content 
5. To Read String Content From File:  write file name 
6. To Clear The Content Of A File: C write file name 
7. To Get The Size Of The Content Of A File:  write folder name 
8. To Get The Size Of The Content Of A Folder: write folder name 
9. To Print The File/folder Names Inside A Folder: write folder name 
10. To Get The Walk Tree Of A Folder: Call The Method tree(): write folder name   
11. To watch Curent Directory just Choose option 11
12. To watch Current Directory Files 


Error Codes: 
********************* 
1. FileNotFoundError: In Case The File We Want To Modify Does Not Exist. 
2. FileExistsError: In Case The File We Want To Create Already Exists. 
3. TypeError: In Case The Location Is Not Written In String.
