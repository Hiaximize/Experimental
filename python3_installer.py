#!/usr/bin/env python

import subprocess as sp

sp.call("apt-get update && apt-get install python3", shell=True)
