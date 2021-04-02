#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""==============================================================================
# Project: MSBench
# Script : paras.py
# Author : Peng Jia
# Date   : 2021.04.02
# Email  : pengjia@stu.xjtu.edu.cn
# Description: TODO
=============================================================================="""
import argparse
import os
import sys

curpath = os.path.abspath(os.path.dirname(sys.argv[0]))
sys.path.append(os.path.dirname(curpath))

from src.benchmark import *
from src.benchmark_merge import benchmark_merge

logger.info("Commands: " + " ".join(sys.argv))


def args_process():
    """
    argument procress
    """
    defaultPara = get_value("default")
    commands = []
    commandsParser = {}
    parser = argparse.ArgumentParser(description='mstools: Microsatellite genotyping toolbox.'
                                     # + ".show help of subcommand with '"
                                     # + get_value("tools_name") + " <subcommand> -h'"
                                     )
    parser.usage = get_value("tools_name") + " <command> [options]"
    parser.add_argument('-V', '--version', action='version',
                        version=get_value("tools_name") + get_value("tools_version"))
    subparsers = parser.add_subparsers(title="command", metavar="", dest='command')
    ###################################################################################################################
    # add arguments for benchmark module
    parser_bm = subparsers.add_parser('benchmark', help='Microsatellite genotyping benchmark using phased assemblies')
    parser_bm.description = 'Microsatellite associate mutaion benchmark.'
    commands.append('benchmark')
    defaultPara_bm = defaultPara["benchmark"]
    ##################################################################################
    # group input and output
    bm_input_and_output = parser_bm.add_argument_group(title="Input and output")
    bm_input_and_output.add_argument('-i', '--input', required=True, type=str, nargs=1,
                                     help="Aligned contig of phased assembly, bam/cram [required]")
    bm_input_and_output.add_argument('-m', '--microsatellite', required=True, type=str, nargs=1,
                                     help="The path of the microsatellite regions [required]")
    bm_input_and_output.add_argument('-o', '--output', required=True, type=str, nargs=1,
                                     help="The path of output file prefix [required]")
    bm_input_and_output.add_argument('-r', '--reference', required=True, type=str, nargs=1,
                                     help="The path of reference file fa/fasta[required]")
    bm_input_and_output.add_argument("-mf", '--microsatellite_region_format', type=str, nargs=1,
                                     choices=["bed", "json", "msisensor_scan"],
                                     default=[defaultPara_bm["microsatellite_region_format"]],
                                     help='Input format of microsatellites region file [default:'
                                          + str(defaultPara_bm["microsatellite_region_format"]) + ']')
    bm_input_and_output.add_argument('-tech', '--technology', type=str, nargs=1,
                                     choices=["ccs", "clr", "ont", "ilm", "contig"],
                                     required=True,
                                     help='Sequencing technology [required]')
    ##################################################################################
    # group general option
    bm_general_option = parser_bm.add_argument_group(title="General option")
    bm_general_option.add_argument('-d', '--debug', type=bool, nargs=1, choices=[True, False],
                                   default=[defaultPara_bm["debug"]],
                                   help="Debug mode for developers [default:" +
                                        str(defaultPara_bm["debug"]) + "]")
    bm_general_option.add_argument('-oh', '--only_homopolymers', type=int, nargs=1, choices=[True, False],
                                   default=[defaultPara_bm["only_homopolymers"]],
                                   help="Only analyze homopolymer regions [default:"
                                        + str(defaultPara_bm["only_homopolymers"]) + "]")
    bm_general_option.add_argument('-pl', '--prefix_len', type=int, nargs=1,
                                   default=[defaultPara_bm["prefix_len"]],
                                   help=" {prefix_len} bps upstream of microsatellite to analysis [default:" +
                                        str(defaultPara_bm["prefix_len"]) + "]")
    bm_general_option.add_argument('-sl', '--suffix_len', type=int, nargs=1,
                                   default=[defaultPara_bm["suffix_len"]],
                                   help=" {suffix_len} bps downstream of microsatellite to analysis [default:" +
                                        str(defaultPara_bm["suffix_len"]) + "]")
    bm_general_option.add_argument('-om', '--only_microsatellites', type=int, nargs=1, choices=[True, False],
                                   default=[defaultPara_bm["only_microsatellites"]],
                                   help="True, only detect variants in microsatelite microsatellite region;"
                                        " False, also detect upstream and downstream variants [default:"
                                        + str(defaultPara_bm["only_microsatellites"]) + "]")
    bm_general_option.add_argument("-minr", '--minimum_repeat_times',
                                   default=[defaultPara_bm["minimum_repeat_times"]],
                                   type=str, nargs=1,
                                   help="Minimum repeat times of microsatellites [default:"
                                        + defaultPara_bm["minimum_repeat_times"] + "]")
    bm_general_option.add_argument('-maxr', '--maximum_repeat_times',
                                   default=[defaultPara_bm["maximum_repeat_times"]], type=str, nargs=1,
                                   help="Maximum repeat times of microsatellites [default:"
                                        + defaultPara_bm["maximum_repeat_times"] + "]")
    bm_general_option.add_argument('-minh', '--minimum_phasing_reads',
                                   default=[defaultPara_bm["minimum_phasing_reads"]], type=str, nargs=1,
                                   help="Minimum reads for each haplotype reporting [default:"
                                        + str(defaultPara_bm["minimum_phasing_reads"]) + "]")

    ##################################################################################
    # group for bam2dis
    bm_bam2dis_option = parser_bm.add_argument_group(title="Option for bam2dis")
    bm_bam2dis_option.add_argument('-q', '--minimum_mapping_quality', type=int, nargs=1,
                                   default=[defaultPara_bm["minimum_mapping_quality"]],
                                   help="minimum mapping quality of read [default:" +
                                        str(defaultPara_bm["minimum_mapping_quality"]) + "]")
    bm_bam2dis_option.add_argument('-s', '--minimum_support_reads', type=int, nargs=1,
                                   default=[defaultPara_bm["minimum_support_reads"]],
                                   help="minimum support reads of an available microsatellite [default:" +
                                        str(defaultPara_bm["minimum_support_reads"]) + "]")
    bm_bam2dis_option.add_argument('-am', '--allow_mismatch', type=bool, nargs=1, choices=[True, False],
                                   default=[defaultPara_bm["allow_mismatch"]],
                                   help="allow mismatch when capture microsatellite [default:"
                                        + str(defaultPara_bm["allow_mismatch"]) + "]")

    ##################################################################################
    # group for multiple_thread

    multiple_thread = parser_bm.add_argument_group(title="Multiple thread")
    multiple_thread.add_argument('-t', '--threads', type=int, nargs=1,
                                 default=[defaultPara_bm["threads"]],
                                 help="The number of  threads to use [default:" +
                                      str(defaultPara_bm["threads"]) + "]")
    multiple_thread.add_argument('-b', '--batch', type=int, nargs=1,
                                 default=[defaultPara_bm["batch"]],
                                 help="The number of microsatellite one thread process [default:" +
                                      str(defaultPara_bm["batch"]) + "]")

    commandsParser["benchmark"] = parser_bm

    # bm_input_and_output.add_argument('-r', '--input', required=True, type=str, nargs=1,
    #                                  help="The path of input bam/cram file [required]")
    # bm_input_and_output.add_argument('-m', '--input', required=True, type=str, nargs=1,
    #                                  help="The path of input bam/cram file [required]")

    ###################################################################################################################
    # add arguments for benchmark module
    parser_bmm = subparsers.add_parser('benchmark_merge', help='Merge two haplotype result.')
    parser_bmm.description = 'Merge two haplotype microsatellite calling result.'
    commands.append('benchmark_merge')
    default_para_bmm = defaultPara["benchmark_merge"]

    ##################################################################################
    # group input and output
    bmm_input_and_output = parser_bmm.add_argument_group(title="Input and output")
    bmm_input_and_output.add_argument('-1', '--hap1', required=True, type=str, nargs=1,
                                      help="microsatellite calling result of haplotype 1, *vcf.gz [required]")
    bmm_input_and_output.add_argument('-2', '--hap2', required=True, type=str, nargs=1,
                                      help="microsatellite calling result of haplotype 2, *vcf.gz [required]")
    bmm_input_and_output.add_argument('-o', '--output', required=True, type=str, nargs=1,
                                      help="The path of output file prefix [required]")
    bmm_input_and_output.add_argument('-s', '--sample', required=False, type=str, nargs=1,
                                      default=[default_para_bmm["sample"]],
                                      help="Sample name[default:" + default_para_bmm["sample"] + "]")
    bmm_general_option = parser_bmm.add_argument_group(title="General option")
    bmm_general_option.add_argument('-d', '--debug', type=bool, nargs=1, choices=[True, False],
                                    default=[default_para_bmm["debug"]],
                                    help="Debug mode for developers [default:" +
                                         str(default_para_bmm["debug"]) + "]")
    if len(os.sys.argv) < 2:
        parser.print_help()
        return False

    if os.sys.argv[1] in ["-h", "--help", "-?"]:
        parser.print_help()
        return False
    if os.sys.argv[1] in ["-V", "-v", "--version"]:
        # parser.print_help()
        parser.parse_args()
        return False
    if os.sys.argv[1] not in commands:
        logger.error("Command Error! " + os.sys.argv[1] +
                     "is not the available command.\n"
                     "[Tips] Please input correct command such as " + ", ".join(commands) + "!")
        parser.print_help()
        # parser.parse_args()
        return False
    if len(os.sys.argv) == 2 and (os.sys.argv[1] in commands):
        commandsParser[os.sys.argv[1]].print_help()
        return False
    return parser
