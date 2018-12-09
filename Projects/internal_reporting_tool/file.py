import codecs


class File():

    FILENAME = "exemple.txt"

    def write(self, text):
        try:
            f = codecs.open(self.FILENAME, "a+", "utf-8")
            f.write('\n'.join(text))
        except:
            print("Could not open file " + self.FILENAME)
        finally:
            f.close()
