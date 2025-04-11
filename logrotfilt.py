#!/usr/bin/env python3

import sys
import os
import argparse

def main():
    """ Program to break input to a series of numbered files with a cutoff

    Write text input to a series of files.  When the split length is exceeded open a new file using the template.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--split", action="store", dest="split", type=float, default=1, help="split size in MB")
    parser.add_argument("--template", action="store", dest="template", required=True, help="output file name template.  Use {} for count placeholder")
    parser.add_argument("-e", "--echo", action="store_true", help="echo lines to stdout")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose output")
    args=parser.parse_args()

    # count of files
    count=0

    while True:
        outputfilename = args.template.format(count)
        if args.verbose:
            print(f"INFO outputfile {outputfilename}")
        with open(outputfilename, "w") as f:
            datasize = 0
            try:
                while True:
                    line = sys.stdin.readline()
                    if not line:
                        if args.verbose:
                            print(f"INFO closing {outputfilename}  and exiting")
                        f.close()
                        return 0
                    if args.echo:
                        print(line, end="")
                        #sys.stdout.flush()
                    f.write(line)
                    f.flush()
                    datasize += len(line)
                    #if args.verbose:
                    #    print(f"INFO datasize {datasize}")
                    if datasize > args.split*1024*1024:
                        if args.verbose:
                            print(f"INFO closing {outputfilename} and continuing to next")
                        break;
            except KeyboardInterrupt:
                # KeyboardInterrupt doesn't inherit from Exception
                print(f"Exiting logrotfilt due to KeyboardInterrupt");
                return
            except Exception as e:
                print(f"ERROR: logrotfilt {e}");
                return
            count += 1

if __name__ == "__main__":
    sys.exit(main())
