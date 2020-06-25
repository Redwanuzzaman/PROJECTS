import logging
logging.basicConfig(filename="logName.txt", level=logging.DEBUG)


class WriteFile:
    def write(self, file_location, content):
        try:
            with open(file_location, "w") as file:
                file.writelines(content)
            logging.info("Successfully Written on " + file_location)
        except Exception as e:
            logging.error("No Such File Found!")
            print("Error! Code: {c}, {m}".format(c=type(e).__name__, m=str(e)))


# wf = WriteFile()
# wf.write("C:/Users/Md Redwanuzzaman/Desktop/file 1.txt", "hello hii..!")
