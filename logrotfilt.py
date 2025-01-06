#!/usr/bin/env python3

import sys
import os
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--split", action="store", dest="split", type=int, default=1, help="split size in MB")
    parser.add_argument("--template", action="store", dest="template", required=True, help="output file name template")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose output")
    args=parser.parse_args()

    # count of files
    count=0

    while True:
        outputfilename = args.template.format(count)
        if args.verbose:
            print(f"INFO outputfile {outputfilename}")
        f =  open(outputfilename, "w") # , buffering=0)
        datasize = 0

        while True:
            line = sys.stdin.readline()
            if not line:
                print(f"INFO closing file and exiting")
                f.close()
                return 0
            f.write(line)
            f.flush()
            datasize += len(line)
            if args.verbose:
                print(f"INFO datasize {datasize}")
            if datasize > args.split*1024*1024:
                print(f"INFO closing file and continuing to next")
                f.close()
                break;
        count += 1

if __name__ == "__main__":
    sys.exit(main())
