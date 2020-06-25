import os
import logging
logging.basicConfig(filename="logName.txt", level=logging.DEBUG)


class FolderSize:

    def folder_size(self, location):
        try:
            files = os.listdir(location)
            logging.info("Successfully Get the size of the folder. It's {}".format(len(files)))
            print(len(files))
        except Exception as e:
            logging.error("No Such Directory Found!")
            print("Error! Code: {c}, {m}".format(c=type(e).__name__, m=str(e)))


# fs = FolderSize()
# print(fs.folder_size("C:/Users/Md Redwanuzzaman/Desktop/car"))