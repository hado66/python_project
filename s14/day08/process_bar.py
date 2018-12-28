#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import time
import sys
file_size=0
file_size_total=102654

for i in range(101):
    sys.stdout.write('\r')
    sys.stdout.write("%s%% |%s" % (int(file_size /file_size_total*100), int(i % 101) * '#'))
    sys.stdout.flush()
    time.sleep(0.3)
    if file_size<file_size_total-1024:
        size=1024
    else:
        size=file_size_total-file_size
    file_size+=size
    if file_size==file_size_total:
        sys.stdout.write('\r')
        sys.stdout.write("%s%% |%s" % (100, 100 * '#'))
        sys.stdout.flush()

    # sys.stdout.write('\n')