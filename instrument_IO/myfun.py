import pyvisa as visa
from helpers.kthread import *
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

    @timeout(5)
    def method_timeout(self, seconds, text):
        print('start', seconds, text)
        sleep(seconds)
        print('finish', seconds, text)
        return seconds

if __name__ == '__main__':
    obj = A()

    for sec in range(1, 10):
        try:
            print('*' * 20)
            print(obj.method_timeout(sec, 'test waiting %d seconds' % sec))
        except Timeout as e:
            print(e)