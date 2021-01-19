import pyvisa as visa

class A(object):

    def __init__(self):
        self.visa_addr = 'GOOD ADDRESS'

    def exceptionHandler(self, exception):
        print(
            'Error information:\n\tAbbreviation: %s\n\tError code: %s\n\tDescription: %s' %
            (exception.abbreviation, exception.error_code, exception.description))

    def handler(self):

        resourceManager = visa.ResourceManager()

        try:
            session = resourceManager.open_resource("BAD ADDRESS")
        except visa.VisaIOError as ex:
            print('VISA ERROR - An error has occurred!\n')
            self.exceptionHandler(ex)

if __name__ == '__main__':
    obj = A()
    obj.handler()
