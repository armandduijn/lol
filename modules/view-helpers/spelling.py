#!/usr/bin/env python

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
#print os.path.dirname(__file__)
from modules.spelling.correction import correction



correct = correction(sys.argv[1])
print correct