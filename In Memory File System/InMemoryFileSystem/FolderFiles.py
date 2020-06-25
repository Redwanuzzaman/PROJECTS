import os
import logging
logging.basicConfig(filename="logName.txt", level=logging.DEBUG)


class FolderFiles:

    def file_list(self, location):
        try:
            files = os.listdir(location)
            files.sort()
            if len(files) == 0:
                print("No Files Yet")
            for file in files:
                print(file)
            logging.info("Successfully Get List of files in: " + location)
        except Exception as e:
            logging.error("No Such Directory Found!")
            print("Error! Code: {c}, {m}".format(c=type(e).__name__, m=str(e)))


# ff = FolderFiles()
# ff.file_list("C:/Users/Md Redwanuzzaman/Desktop")
