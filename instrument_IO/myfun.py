import pyvisa as visa


def exceptionHandler(exception):

    print(
        'Error information:\n\tAbbreviation: %s\n\tError code: %s\n\tDescription: %s' %
        (exception.abbreviation, exception.error_code, exception.description))


# Change this variable to the address of your instrument
VISA_ADDRESS = 'Your instruments VISA address goes here!'

# Part 1:
#
# Shows the mechanics of how to deal with an error in PyVISA when it occurs.
# To stimulate an error, the code will try to open a connection to an instrument at an invalid address...
#
# First we'll provide an invalid address and see what error we get

resourceManager = visa.ResourceManager()

try:
    session = resourceManager.open_resource("BAD ADDRESS")
except visa.VisaIOError as ex:
    print('VISA ERROR - An error has occurred!\n')

    # To get more specific information about the exception, we can check what kind of error it is and
    # add specific error handling code. In this example, that is done in the
    # exceptionHandler function
    exceptionHandler(ex)