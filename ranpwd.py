#!/usr/bin/python

import string,random

alphabet = string.ascii_letters + string.digits + string.punctuation
a = "".join(random.choice(alphabet) for x in range(8))
print a
