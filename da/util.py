# -*- coding: utf-8 -*-
"""
Various utilities


"""
import copy
import datetime
import logging
import math
import os
import pickle
import random
import socket
import sys
from collections import Counter, OrderedDict
from logging.handlers import TimedRotatingFileHandler

import toml

print("os.getcwd", os.getcwd())


################### Global VAR Logs ################################################################
APP_ID = __file__ + "," + str(os.getpid()) + "," + str(socket.gethostname())
APP_ID2 = str(os.getpid()) + "_" + str(socket.gethostname())

LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logfile.log")
FORMATTER_1 = logging.Formatter("%(asctime)s,  %(name)s, %(levelname)s, %(message)s")
FORMATTER_2 = logging.Formatter("%(asctime)s.%(msecs)03dZ %(levelname)s %(message)s")
FORMATTER_3 = logging.Formatter("%(asctime)s  %(levelname)s %(message)s")
FORMATTER_4 = logging.Formatter("%(asctime)s, %(process)d, %(filename)s,    %(message)s")

FORMATTER_5 = logging.Formatter(
    "%(asctime)s, %(process)d, %(pathname)s%(filename)s, %(funcName)s, %(lineno)s,  %(message)s"
)


def os_make_dirs(filename):
    folder = os.path.dirname(filename)
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder


####################################################################################################
def save_all(variable_list, folder, globals_main=None):
    for x in variable_list:
        try:
            filename = save(globals_main[x], folder + x + ".pkl")
            print(filename)
        except Exception as e:
            print("error", e)


def save(obj, filename="/folder1/keyname", isabsolutpath=0):
    """
    :param obj:
    :param filename:
    :param isabsolutpath:
    :return:
    """
    folder = os_make_dirs(filename)

    with open(filename, "wb") as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
    return filename


def load(filename="/folder1/keyname", isabsolutpath=0, encoding1="utf-8"):
    """

    :param filename:
    :param isabsolutpath:
    :param encoding1:
    :return:
    """
    folder = os_make_dirs(filename)
    with open(filename, "rb") as f:
        return pickle.load(f)


####################################################################################################
def create_appid(filename):
    # appid  = filename + ',' + str(os.getpid()) + ',' + str( socket.gethostname() )
    appid = filename + "," + str(os.getpid())
    return appid


def create_logfilename(filename):
    return filename.split("/")[-1].split(".")[0] + ".log"


def create_uniqueid():
    return datetime.datetime.now().strftime("_%Y%m%d%H%M%S_") + str(random.randint(1000, 9999))


####################################################################################################
################### Logger #########################################################################
def logger_setup(
    logger_name=None,
    log_file=None,
    formatter=FORMATTER_1,
    isrotate=False,
    isconsole_output=True,
    logging_level=logging.DEBUG,
):
    """
    my_logger = util_log.logger_setup("my module name", log_file="")
    APP_ID    = util_log.create_appid(__file__ )
    def log(*argv):
      my_logger.info(",".join([str(x) for x in argv]))
  
   """

    if logger_name is None:
        logger = logging.getLogger()  # Gets the root logger
    else:
        logger = logging.getLogger(logger_name)

    logger.setLevel(logging_level)  # better to have too much log than not enough

    if isconsole_output:
        logger.addHandler(logger_handler_console(formatter))

    if log_file is not None:
        logger.addHandler(
            logger_handler_file(formatter=formatter, log_file_used=log_file, isrotate=isrotate)
        )

    # with this pattern, it's rarely necessary to propagate the error up to parent
    logger.propagate = False
    return logger


def logger_handler_console(formatter=None):
    formatter = FORMATTER_1 if formatter is None else formatter
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    return console_handler


def logger_handler_file(isrotate=False, rotate_time="midnight", formatter=None, log_file_used=None):
    formatter = FORMATTER_1 if formatter is None else formatter
    log_file_used = LOG_FILE if log_file_used is None else log_file_used
    if isrotate:
        print("Rotate log", rotate_time)
        fh = TimedRotatingFileHandler(log_file_used, when=rotate_time)
        fh.setFormatter(formatter)
        return fh
    else:
        fh = logging.FileHandler(log_file_used)
        fh.setFormatter(formatter)
        return fh


def logger_setup2(name=__name__, level=None):
    _ = level

    # logger defines
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


####################################################################################################
################### Print ##########################################################################
def printlog(
    s="",
    s1="",
    s2="",
    s3="",
    s4="",
    s5="",
    s6="",
    s7="",
    s8="",
    s9="",
    s10="",
    app_id="",
    logfile=None,
    iswritelog=True,
):
    try:
        if app_id != "":
            prefix = app_id + "," + datetime.datetime.now().strftime("_%Y%m%d%H%M%S_")
        else:
            prefix = APP_ID + "," + datetime.datetime.now().strftime("_%Y%m%d%H%M%S_")
        s = ",".join(
            [
                prefix,
                str(s),
                str(s1),
                str(s2),
                str(s3),
                str(s4),
                str(s5),
                str(s6),
                str(s7),
                str(s8),
                str(s9),
                str(s10),
            ]
        )

        print(s)
        if writelog:
            writelog(s, logfile)
    except Exception as e:
        print(e)
        if iswritelog:
            writelog(str(e), logfile)


def writelog(m="", f=None):
    f = LOG_FILE if f is None else f
    with open(f, "a") as _log:
        _log.write(m + "\n")


####################################################################################################
def load_arguments(config_file=None, arg_list=None):
    """
      Load CLI input, load config.toml , overwrite config.toml by CLI Input
      [{}, {}]
    """
    import toml
    import argparse

    if config_file is not None:
        cur_path = os.path.dirname(os.path.realpath(__file__))
        config_file = os.path.join(cur_path, "config.toml")

    p = argparse.ArgumentParser()
    p.add_argument("--config_file", default=config_file, help="Params File")
    p.add_argument("--config_mode", default="test", help=" test/ prod /uat")
    for x in arg_list:
        p.add_argument(x["--"], default=x.get("default"), help=x.get("help"))

    arg = p.parse_args()

    # Load file params as dict namespace
    class to_name(object):
        def __init__(self, adict):
            self.__dict__.update(adict)

    print(arg.config_file)
    pars = toml.load(arg.config_file)
    pars = pars[arg.config_mode]  # test / prod
    print(arg.config_file, pars)

    ### Overwrite params by CLI input and merge with toml file
    for key, x in vars(arg).items():
        if x is not None:  # only values NOT set by CLI
            pars[key] = x

    # print(pars)
    pars = to_name(pars)  #  like object/namespace pars.instance
    return pars
