#!/usr/bin/env python3
import codecs


class File():
    """ This File class provides a mechanism to save text files. """

    # filename
    FILENAME = "exemple.txt"

    def write(self, question, query_result):
        """
        This write method is responsible for write a text on the file
        
        It recives as paramiter:
            The text to be written:
                question
                query_result
        """

        try:
            f = codecs.open(self.FILENAME, "a+", "utf-8")
            f.write(self.__format_text(question, query_result))
        except IOError as err:
            print("Could not open file {} - {}".format(self.FILENAME, err))
        finally:
            f.close()

    def __format_text(self, question, query_result):
        """
        This __format_text private method is responsible for formating the text is going to be written on the file
        
        It recives as paramiter:
            The text to be formated:
                question
                query_result
        It returns the formated text
        """

        return question + '\n' + '\r\n'.join(map(str, query_result)) + '\n\n'
