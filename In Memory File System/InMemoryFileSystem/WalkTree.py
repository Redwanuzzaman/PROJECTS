import os
import logging
logging.basicConfig(filename="logName.txt", level=logging.DEBUG)


class WalkTree:
    def tree(self, location):
        try:
            for root_dir, sub, files in os.walk(location):
                sub = [n for n in sub]
                files = [n for n in files]

                for file in files:
                    print(file)
                for file in sub:
                    print(file)
            logging.info("Successfully Generated Walk Tree in: " + location)
        except Exception as e:
            logging.error("No Such Directory Found!")
            print("Error! Code: {c}, {m}".format(c=type(e).__name__, m=str(e)))


# wt = WalkTree()
# wt.tree("C:/Users/Md Redwanuzzaman/Desktop/")
