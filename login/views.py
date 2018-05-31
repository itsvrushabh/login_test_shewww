from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from login.service import ConnectionHandler
from login.serializers import LoginDetailSerializers

# Create your views here.


class LoginService(GenericAPIView):
    """
    **Use Cases**
        Request Enrollment Lists for a course
    **Example Requests**
        POST /api/login/
    **Response Values**
        Body consists of the list of users of the course  of following fields:
        message : output, exception of router
        result : result is true or false
        status : status of config
        record_id : mongo id from mongodb
    **Parameters:**
        username: Router Username of the router
        password: Router Password of the router
        host: Ip address of host router
        device_type : Device Type of the router
    **Returns**
        * 200 on success with above fields.
        * 400 if an invalid parameter was sent
        Example response:
            [
              {
                "message": ""
                "status": "",
                "result": "",
                "record_id": "",
              }
            ]
    """
    queryset = ''
    serializer_class = LoginDetailSerializers

    def get(self, request, format=True):
        return Response({'data': 'call'})

    def post(self, request, format=True):
        serializer = LoginDetailSerializers(data=request.data)
        if serializer.is_valid():
            detail = {
                'host': serializer['host'].value,
                'username': serializer['username'].value,
                'password': serializer['password'].value,
                'device_type': serializer['device_type'].value
                }
            _output = {'Error': detail}
        else:
            _output = {'Error post api': serializer.errors}
        return Response(_output)
