#!/usr/bin/python
import sys


def reducer():
    '''
    Given the output of the mapper for this exercise, the reducer should PRINT
    (not return) one line per UNIT along with the total number of ENTRIESn_hourly
    over the course of May (which is the duration of our data), separated by a tab.
    An example output row from the reducer might look like this: 'R001\t500625.0'

    You can assume that the input to the reducer is sorted such that all rows
    corresponding to a particular UNIT are grouped together.

    Since you are printing the output of your program, printing a debug
    statement will interfere with the operation of the grader. Instead,
    use the logging module, which we've configured to log to a file printed
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    '''
    old_key = None
    total_entries = 0.0
    for line in sys.stdin:
        data = line.strip().split('\t')
        if len(data) != 2:
            continue
        new_key, entries = data
        if old_key and new_key != old_key:
            print old_key, '\t', total_entries
            total_entries = 0.0
        old_key = new_key
        total_entries += float(entries)
    if old_key is not None:
        print old_key,'\t', total_entries




reducer()
