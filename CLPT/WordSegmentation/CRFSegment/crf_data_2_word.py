#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 52nlpcn@gmail.com
# Copyright 2014 @ YuZhen Technology
#
# 4 tags for character tagging: B(Begin), E(End), M(Middle), S(Single)

import codecs
import sys



def character_2_word(input_file, output_file):
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')
    is_first = True
    for line in input_data.readlines():
        if line == "\n":
            if is_first == True:
                output_data.write("\r\n")
            else:
                output_data.write(" \r\n")
            is_first = True
        else:
            char_tag_pair = line.strip().split('\t')
            char = char_tag_pair[0]
            tag = char_tag_pair[1]
            if tag == 'B':
                if is_first == True:
                    output_data.write(char)
                    is_first = False
                else:
                    output_data.write(' ' + char)
            elif tag == 'M':
                output_data.write(char)
            elif tag == 'E':
                output_data.write(char + ' ')
            else: # tag == 'S'
                if is_first == True:
                    output_data.write(char + ' ')
                    is_first = False
                else:
                    output_data.write(' ' + char + ' ')
    input_data.close()
    output_data.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "pls use: python crf_data_2_word.py input output"
        sys.exit()
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    character_2_word(input_file, output_file)
