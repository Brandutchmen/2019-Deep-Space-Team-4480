#!/usr/bin/python
# -*- coding: utf-8 -*-

import wpilib
import math

class PrintColor(object):

    def __init__(self):
        pass

    def printRed(self, text):
        print('\033[91m' + text + '\033[0m')

    def printCyan(self, text):
        print('\033[96m' + text + '\033[0m')

    def printBlue(self, text):
        print('\033[94m' + text + '\033[0m')

    def printGreen(self, text):
        print('\033[92m' + text + '\033[0m')

    def printYellow(self, text):
        print('\033[93m' + text + '\033[0m')

    def printBold(self, text):
        print('\033[1m' + text + '\033[0m')
