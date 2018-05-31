from netmiko import Netmiko


class ConnectionHandler:
    def __init__(self, logindetail):
        try:
            self.logindetail = logindetail
            self.connection = None
        except Exception as exception:
            print('Error : ', exception.args)

    def connect_router(self):
        try:
            connection = Netmiko(**self.logindetail)
            self.connection = connection
        except Exception as exception:
            print("Error : ", exception)
        return self.connection

    def disconnect_router(self):
        try:
            self.connection.disconnect()
        except Exception as exception:
            print("error : "+str(exception.args))

    def valid_router(self):
        _flag = False
        try:
            if self.connection.is_alive():
                _flag = True
        except Exception as exception:
            print('error : '+str(exception.args))
        return _flag
