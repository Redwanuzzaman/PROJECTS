import logging
logging.basicConfig(filename="logName.txt", level=logging.DEBUG)


class ReadFile:

    def read(self, file_location):
        try:
            with open(file_location, "r") as file:
                for line in file:
                    print(line, end='')
                print()
            logging.info("Successfully Read From: " + file_location)
        except Exception as e:
            logging.error("No Such File Found!")
            print("Error! Code: {c}, {m}".format(c=type(e).__name__, m=str(e)))


# rf = ReadFile()
# rf.read("C:/Users/Md Redwanuzzaman/Desktop/file_name.txt")
