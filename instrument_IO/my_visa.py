import pyvisa as visa

# 目标
# 定义网分对象
# 封装常见操作，read / write / query
# 考虑异常处理


class MyError(Exception):

    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class MyResource(object):

    def __init__(self,
                 visa_addr=None,
                 timeout=2000,
                 write_termination='\n',
                 **kwargs):

        self.visa_addr = '' if visa_addr is None else visa_addr
        self.read_timeout = timeout
        self.termination = write_termination
        self.session = None

    def open_resource(self):
        self.rm = visa.ResourceManager()
        try:
            self.session = self.rm.open_resource(self.visa_addr)
            print(self.session.write_termination)
            print(self.session.timeout)
            #self.session.read_termination
        except (visa.VisaIOError, ValueError, OSError) as ex:
            print('Error Info:\n{}'.format(ex))

        self.session.close()
        self.rm.close()
conf = {
    'visa_addr':'TCPIP0::192.168.1.3::inst0::INSTR'
}
a = MyResource(**conf)
a.open_resource()
#print(a.__dict__)

