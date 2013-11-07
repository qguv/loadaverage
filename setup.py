#!/usr/bin/env python3
# rpcalc setup script
# for more info, see github.com/qguv/rpcalc

from distutils.core import setup

if __name__ == '__main__':
    setup(  name = "LoadAverage",
            version = "0.1",
            description = "Simple Multi-Purpose Adjusted Load Averages",
            author = "Quint Guvernator",
            author_email = "quintus.public@gmail.com",
            url = "https://github.com/qguv/loadaverage",
            scripts = ["scripts/load"],
            packages = ["load"],
    )
