from crawler.color import Colored

__color = Colored()

LEVEL_NONE = 0
LEVEL_DEBUG = 1
LEVEL_INFO = 2
LEVEL_ERROR = 3
LEVEL_WARNING = 4

PRINT_LEVEL = LEVEL_NONE


def e(msg):
    if LEVEL_ERROR >= PRINT_LEVEL:
        print(__color.red(msg))


def d(msg):
    if LEVEL_DEBUG >= PRINT_LEVEL:
        print(__color.blue(msg))


def i(msg):
    if LEVEL_INFO >= PRINT_LEVEL:
        print(__color.green(msg))


def w(msg):
    if LEVEL_WARNING >= PRINT_LEVEL:
        print(__color.yellow(msg))
