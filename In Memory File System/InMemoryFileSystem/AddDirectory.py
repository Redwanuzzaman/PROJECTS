import shutil
import logging
logging.basicConfig(filename="logName", level=logging.DEBUG)


class AddDirectory:

    def add(self, source, destination):
        try:
            shutil.move(source, destination)
            logging.info("File Successfully Moved to " + destination)
        except Exception as e:
            logging.error("Failed to Move to " + destination)
            print("Error! Code: {c}, {m}".format(c = type(e).__name__, m=str(e)))


# ad = AddDirectory()
# ad.add("C:/Users/Md Redwanuzzaman/Desktop/projrct images", "C:/Users/Md Redwanuzzaman/Desktop/Coursera")
