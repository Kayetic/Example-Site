import openai
import os
import json
import sys
import time
import random
import string
import requests
import re
import datetime
import time


# write a fibbonaci function non recursive

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
