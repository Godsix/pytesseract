from enum import IntEnum
from ctypes import Structure, POINTER, c_int, c_float
from .pix import LPPix, LPPixa, LPPixaa, LPPta
from .array_h import LPNuma, LPSarray, LPL_DnaHash


class JBClassifier(IntEnum):
    '''JB Classifier'''
    JB_RANKHAUS = 0
    JB_CORRELATION = 1


class JBComponent(IntEnum):
    '''JB Component'''
    JB_CONN_COMPS = 0
    JB_CHARACTERS = 1
    JB_WORDS = 2


class JbClasser(Structure):
    '''
    The JbClasser struct holds all the data accumulated during the
    classification process that can be used for a compressed
    jbig2-type representation of a set of images.  This is created
    in an initialization process and added to as the selected components
    on each successive page are analyzed.
    '''
    _fields_ = [
        ("safiles", LPSarray),   # input page image file names
        ("method", c_int),   # JB_RANKHAUS, JB_CORRELATION
        ("components", c_int),   # JB_CONN_COMPS, JB_CHARACTERS or
        ("maxwidth", c_int),   # max component width allowed
        ("maxheight", c_int),   # max component height allowed
        ("npages", c_int),   # number of pages already processed
        ("baseindex", c_int),   # number components already processed
        ("nacomps", LPNuma),   # number of components on each page
        ("sizehaus", c_int),   # size of square struct elem for haus
        ("rankhaus", c_float),   # rank val of haus match, each way
        ("thresh", c_float),   # thresh value for correlation score
        ("weightfactor", c_float),   # corrects thresh value for heaver
        ("naarea", LPNuma),   # w * h of each template, without
        ("w", c_int),   # max width of original src images
        ("h", c_int),   # max height of original src images
        ("nclass", c_int),   # current number of classes
        ("keep_pixaa", c_int),   # If zero, pixaa isn't filled
        ("pixaa", LPPixaa),   # instances for each class; unbordered
        ("pixat", LPPixa),   # templates for each class; bordered
        ("pixatd", LPPixa),   # templates for each class; bordered
        ("dahash", LPL_DnaHash),   # Hash table to find templates by size
        ("nafgt", LPNuma),   # fg areas of undilated templates;
        ("ptac", LPPta),   # centroids of all bordered cc
        ("ptact", LPPta),   # centroids of all bordered template cc
        ("naclass", LPNuma),   # array of class ids for each component
        ("napage", LPNuma),   # array of page nums for each component
        ("ptaul", LPPta),   # array of UL corners at which the
        ("ptall", LPPta)  # similar to ptaul, but for LL corners
    ]


LPJbClasser = POINTER(JbClasser)
LPLPJbClasser = POINTER(LPJbClasser)


class JbData(Structure):
    '''
    The JbData struct holds all the data required for
    the compressed jbig-type representation of a set of images.
    The data can be written to file, read back, and used
    to regenerate an approximate version of the original,
    which differs in two ways from the original:
      (1) It uses a template image for each c.c. instead of the
          original instance, for each occurrence on each page.
      (2) It discards components with either a height or width larger
          than the maximuma, given here by the lattice dimensions
          used for storing the templates.
    '''
    _fields_ = [
        ("pix", LPPix),   # template composite for all classes
        ("npages", c_int),   # number of pages
        ("w", c_int),   # max width of original page images
        ("h", c_int),   # max height of original page images
        ("nclass", c_int),   # number of classes
        ("latticew", c_int),   # lattice width for template composite
        ("latticeh", c_int),   # lattice height for template composite
        ("naclass", LPNuma),   # array of class ids for each component
        ("napage", LPNuma),   # array of page nums for each component
        ("ptaul", LPPta)  # array of UL corners at which the
    ]


LPJbData = POINTER(JbData)
LPLPJbData = POINTER(LPJbData)
