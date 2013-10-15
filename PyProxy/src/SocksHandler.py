# -*- coding:utf-8 -*-
'''
Created on 2013-10-9

@author: DeadSakura
'''

import SocketServer,httplib

class SocksHandler(SocketServer.StreamRequestHandler):
    '''
    处理Socks协议请求。仅支持Socks5.
    '''


    def __init__(self,params):
        '''
        Constructor
        '''
        