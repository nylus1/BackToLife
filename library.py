import os
import binascii
import ctypes
import string

hexaToExtension = {'.jpg':'JFIF',
                   '.mp4':'',
                   '.extension':'',
                   '.extension':'',
                   '.extension':'',
                   '.extension':'',
                   '.extension':'',
                   '.extension':'',
                   }

def listar_discos():
    '''Funcion para listar los discos que tiene tu PC:\n
    ['C','D','E','G']'''
    drives = []
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives