#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""==============================================================================
# Project: MSHunter
# Script : main.py
# Author : Peng Jia
# Date   : 2020.07.13
# Email  : pengjia@stu.xjtu.edu.cn
# Description: main function and arguments processing
=============================================================================="""
from src.paras import *
from src.benchmark import *
from src.benchmark_merge import *


def main():
    """
    Main function.
    :return:
    """
    global_init()
    arg = args_process()

    if arg:
        parase = arg.parse_args()
        if parase.command == "benchmark":
            benchmark(parase)
        if parase.command == "benchmark_merge":
            benchmark_merge(parase)


if __name__ == "__main__":
    main()
