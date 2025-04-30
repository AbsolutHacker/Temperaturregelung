DEBUG = 0
INFO = 1
WARN = 2

LEVEL = DEBUG


def log(level, msg):
    if level >= LEVEL:
        print(msg)


def debug(msg):
    log(DEBUG, '[DEBUG] ' + msg)


def info(msg):
    log(INFO, msg)


def warn(msg):
    log(WARN, '[WARN] ' + msg)
