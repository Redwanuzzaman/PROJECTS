import logging
logging.basicConfig(filename="logName", level=logging.DEBUG)


class ClearFile:
    def clear(self, file_location):
        try:
            with open(file_location, "w") as file:
                file.write('')
            logging.info("Successfully Cleared the File on: " + file_location)
        except Exception as e:
            logging.error("No Such File Found!")
            print("Error! Code: {c}, {m}".format(c=type(e).__name__, m=str(e)))


# cf = ClearFile()
# cf.clear("C:/Users/Md Redwanuzzaman/Desktop/file 1.txt")
