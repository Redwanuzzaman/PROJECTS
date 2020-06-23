import logging
logging.basicConfig(level=logging.DEBUG)


class CreateFile:
    def create_file(self, file_name):
        try:
            with open(file_name, "w+"):
                pass
            logging.info("Successfully Created File")
        except Exception as e:
            logging.error("Path Error")
            print("Error! Code: {c}, {m}".format(c=type(e).__name__, m=str(e)))


cf = CreateFile()
cf.create_file("file 1.txt")
