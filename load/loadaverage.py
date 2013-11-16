#!/usr/bin/env python3

import subprocess, re, argparse

# Getting number of cores
try:
    # cores command for Linux
    cores = int(subprocess.check_output(['nproc']))
except ( subprocess.CalledProcessError, FileNotFoundError ):
    try:
        # cores command for OS X
        cores = int(subprocess.check_output(['sysctl', '-n', 'hw.ncpu']))
    except:
        raise subprocess.CalledProcessError('your system is not yet supported')

# Getting output from system 'uptime' command for load averages
uptimeOutput = str(subprocess.check_output(['uptime']))

# Builds a regex which looks for a group of three floating-point numbers,
# optionally separated by ' ' and/or ','.
expression = r'([0-9]+\.[0-9]{2},* *){3}'
uptimeOutputSearch = re.search(expression, uptimeOutput)

loadAveragesRaw = uptimeOutputSearch.group(0)

if ', ' in loadAveragesRaw:
    loadAveragesSplit = loadAveragesRaw.split(', ')
elif ',' in loadAveragesRaw:
    loadAveragesSplit = loadAveragesRaw.split(',')
else:
    loadAveragesSplit = loadAveragesRaw.split(' ')

loadAverages = [ float(x) for x in loadAveragesSplit ]
adjustedLoad = [ float(x) / cores for x in loadAveragesSplit ]

# Setting up command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--adjusted",
                        help="displays adjusted load averages",
                        action="store_true")
parser.add_argument("-r", "--raw",
                        help="displays un-adjusted (raw) load averages",
                        action="store_true")
parser.add_argument("-c", "--cores",
                        help="displays number of cores",
                        action="store_true")
verbosity = parser.add_mutually_exclusive_group()
verbosity.add_argument("-v", "--verbose",
                        help="more verbose output",
                        action="count",
                        default=0)
verbosity.add_argument("-q", "--quiet",
                        help="less verbose output",
                        action="store_true")
args = parser.parse_args()

def main():
    # If adjusted is given or no mode specified, give adjusted averages
    if args.adjusted or not args.cores and not args.raw:
        if args.verbose >= 2:
            print("adjusted load averages:", end=' ')
        elif args.verbose >= 1:
            print("adj:", end=' ')
        print('{0[0]:.2f} {0[1]:.2f} {0[2]:.2f}'.format(adjustedLoad).
                replace('.',","))
    if args.raw:
        if args.verbose >= 2:
            print("raw load averages:", end=' ')
        elif args.verbose >= 1:
            print("raw:", end=' ')
        print('{0[0]:.2f} {0[1]:.2f} {0[2]:.2f}'.format(loadAverages, cores))
    if args.cores:
        if args.quiet:
            print(cores)
        else:
            print(cores, "cores")

if __name__ == "__main__":
    main()

