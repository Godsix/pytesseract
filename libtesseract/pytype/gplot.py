from enum import IntEnum
from ctypes import Structure, POINTER, c_int, c_char_p
from .array_h import LPNuma, LPSarray


class GPLOT_STYLE(IntEnum):
    GPLOT_LINES = 0
    GPLOT_POINTS = 1
    GPLOT_IMPULSES = 2
    GPLOT_LINESPOINTS = 3
    GPLOT_DOTS = 4


class GPLOT_OUTPUT(IntEnum):
    GPLOT_NONE = 0
    GPLOT_PNG = 1
    GPLOT_PS = 2
    GPLOT_EPS = 3
    GPLOT_LATEX = 4
    GPLOT_PNM = 5


class GPLOT_SCALING(IntEnum):
    GPLOT_LINEAR_SCALE = 0  # default
    GPLOT_LOG_SCALE_X = 1
    GPLOT_LOG_SCALE_Y = 2
    GPLOT_LOG_SCALE_X_Y = 3


class GPlot(Structure):
    '''Data structure for generating gnuplot files'''
    _fields_ = [
        ("rootname", c_char_p),   # for cmd, data, output
        ("cmdname", c_char_p),   # command file name
        ("cmddata", LPSarray),   # command file contents
        ("datanames", LPSarray),   # data file names
        ("plotdata", LPSarray),   # plot data (1 string/file)
        ("plotlabels", LPSarray),   # label for each individual plot
        ("plotstyles", LPNuma),   # plot style for individual plots
        ("nplots", c_int),   # current number of plots
        ("outname", c_char_p),   # output file name
        ("outformat", c_int),   # GPLOT_OUTPUT values
        ("scaling", c_int),   # GPLOT_SCALING values
        ("title", c_char_p),   # optional
        ("xlabel", c_char_p),   # optional x axis label
        ("ylabel", c_char_p)  # optional y axis label
    ]


LPGPlot = POINTER(GPlot)
LPLPGPlot = POINTER(LPGPlot)
