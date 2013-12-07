#!/usr/bin/env python3
# loadaverage setup script
# for more info, see github.com/qguv/loadaverage

from distutils.core import setup

if __name__ == '__main__':
    setup(  name = "loadaverage",
            version = "0.1.1",
            description = "Simple Multi-Purpose Adjusted Load Averages",
            author = "Quint Guvernator",
            author_email = "quintus.public@gmail.com",
            url = "https://github.com/qguv/loadaverage",
            scripts = ["scripts/load"],
            packages = ["load"],
    )
