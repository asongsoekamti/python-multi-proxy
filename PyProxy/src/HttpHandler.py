# -*- coding:utf-8 -*-
'''
Created on 2013-10-9

@author: DeadSakura
'''

import SocketServer,httplib

class HttpHandler(SocketServer.StreamRequestHandler):
    '''
    处理HTTP（S)协议
    '''


    def __init__(self,header):
        '''
        根据传来的HTTP头重新构造请求，并转送到服务器。
        '''
        