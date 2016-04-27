# -*- coding: UTF-8 -*-

import sys
import re
import time


def wordCount(file_in):
    file_in = open(file_in, 'r')
    file_out = open('result', 'w')
    words = {}
    tic = time.clock()
    for line in file_in:
        line = re.sub('[^(a-zA-Z)+\ \']+', " ", line)
        line_words = line.split()
        for word in line_words:
            if word in words.keys():
                words[word] += 1
            else:
                words[word] = 1
    toc = time.clock()
    print "time it takes is: " + str(toc - tic)
    for word in words:
        file_out.write(word + "\t:\t" + str(words[word]) + '\n')
    file_in.close()
    file_out.close()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        file_in = 'dubliners'
    else:
        file_in = sys.argv[1]
    wordCount(file_in)
