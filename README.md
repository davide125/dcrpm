# dcrpm
dcrpm ("detect and correct rpm") is a tool to detect and correct common issues around RPM database corruption. It attempts a query against your RPM database and runs db4's `db_recover` if it's hung or otherwise seems broken. It then kills any jobs which had the RPM db open previously since they will be stuck in infinite loops within libdb and can't recover cleanly.

## Usage
Run `dcrpm` with no option to detect and correct any outstanding issues with RPM on your host. Additional options can be used to customize logging or select specific remediations. dcrpm is meant to be run from cron regularly to keep things happy and healthy.

## Requirements
dcrpm requires Python 2.7 and psutil. It should work on any Linux distribution with RPM and on Mac OS X.

## Building and installing dcrpm
The easiest way to install dcrpm is by using pip:

    pip install -r requirements.txt # get psutil
    python setup.py install

## Contribute
See the CONTRIBUTING file for how to help out.

## License
dcrpm is GPLv2-licensed.
