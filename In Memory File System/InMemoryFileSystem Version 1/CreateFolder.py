import os
import logging
logging.basicConfig(level=logging.DEBUG)


class CreateFolder:

    def folder(self, location):
        try:
            os.makedirs(os.path.join(location))
            logging.info("Successfully Created Folder in " + location)
        except Exception as e:
            logging.error("No Such Directory Found!")
            print("Error! Code: {c}, {m}".format(c=type(e).__name__, m=str(e)))


# cf = CreateFolder()
# cf.folder("C:/Users/Md Redwanuzzaman/Desktop/tf")
