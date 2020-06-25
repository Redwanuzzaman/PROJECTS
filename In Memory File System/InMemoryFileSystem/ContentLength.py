import logging
logging.basicConfig(filename="logName", level=logging.DEBUG)


class ContentLength:
    def get_length(self, file_location):
        try:
            with open(file_location, "r") as file:
                print(len(file.read()))
                logging.info("Successfully Retrieved the File Size")
        except Exception as e:
            logging.error("No Such File Found!")
            print("Error! Code: {c}, {m}".format(c=type(e).__name__, m=str(e)))


# cl = ContentLength()
# print(cl.get_length("C:/Users/Md Redwanuzzaman/Desktop/file 1.txt"))
