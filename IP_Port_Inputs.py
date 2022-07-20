# Developer : Lucas Liu
# Date: 6/10/2022 Time: 11:18 AM

class IPAndPortInputs:

    def __init__(self, num, obj_name, ip, port):
        self.__id = num
        self.__obj_name = obj_name
        self.__ip = ip
        self.__port = port

    def get_id(self):
        return self.__id

    def get_obj_name(self):
        return self.__obj_name

    def get_ip(self):
        return self.__ip

    def get_port(self):
        return self.__port

    def set_ip(self, ip):
        self.__ip = ip

    def set_port(self, port):
        self.__port = port

    def set_id(self, num):
        self.__id = num

    def set_obj_name(self, obj_name):
        self.__obj_name = obj_name
