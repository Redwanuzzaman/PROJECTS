import logging
logging.basicConfig(filename="logName.txt", level=logging.DEBUG)


class CreateFile:
    def create_file(self, file_location):
        try:
            with open(file_location, "w+"):
                pass
            logging.info("Successfully Created File")
        except Exception as e:
            logging.error("Path Error")
            print("Error! Code: {c}, {m}".format(c=type(e).__name__, m=str(e)))


# cf = CreateFile()
# cf.create_file("file 1.txt")
