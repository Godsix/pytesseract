from enum import IntEnum
from ctypes import Structure, c_int, c_float, c_char_p, POINTER
from ..datatype import c_int_p, c_float_p
from .pix import LPPix, LPPixa, LPPixaa, LPBoxa, LPPta, LPPtaa
from .array_h import LPNuma, LPNumaa, LPSarray, LPL_Dna
from .bmf import LPL_Bmf


class CharacterSet(IntEnum):
    '''Character Set'''
    L_UNKNOWN = 0  # character set type is not specified
    L_ARABIC_NUMERALS = 1  # 10 digits
    L_LC_ROMAN_NUMERALS = 2  # 7 lower-case letters (i,v,x,l,c,d,m)
    L_UC_ROMAN_NUMERALS = 3  # 7 upper-case letters (I,V,X,L,C,D,M)
    L_LC_ALPHA = 4  # 26 lower-case letters
    L_UC_ALPHA = 5  # 26 upper-case letters


class TemplateSelect(IntEnum):
    '''Template Select'''
    L_USE_ALL_TEMPLATES = 0  # use all templates; default
    L_USE_AVERAGE_TEMPLATES = 1  # use average templates; special cases


class L_Rch(Structure):
    '''
    Data returned from correlation matching on a single character
    '''
    _fields_ = [
        ("index", c_int),   # index of best template
        ("score", c_float),   # correlation score of best template
        ("text", c_char_p),   # character string of best template
        ("sample", c_int),   # index of best sample (within the best
        ("xloc", c_int),   # x-location of template (delx + shiftx)
        ("yloc", c_int),   # y-location of template (dely + shifty)
        ("width", c_int)  # width of best template
    ]


LPL_Rch = POINTER(L_Rch)
LPLPL_Rch = POINTER(LPL_Rch)


class L_Rcha(Structure):
    '''
    Data returned from correlation matching on an array of characters
    '''
    _fields_ = [
        ("naindex", LPNuma),   # indices of best templates
        ("nascore", LPNuma),   # correlation scores of best templates
        ("satext", LPSarray),   # character strings of best templates
        ("nasample", LPNuma),   # indices of best samples
        ("naxloc", LPNuma),   # x-locations of templates (delx + shiftx)
        ("nayloc", LPNuma),   # y-locations of templates (dely + shifty)
        ("nawidth", LPNuma)  # widths of best templates
    ]


LPL_Rcha = POINTER(L_Rcha)
LPLPL_Rcha = POINTER(LPL_Rcha)


class L_Rdid(Structure):
    '''
  Data used for decoding a line of characters.
'''
    _fields_ = [
        ("pixs", LPPix),   # clone of pix to be decoded
        # count array for each averaged template
        ("counta", POINTER(c_int_p)),
        # best y-shift array per average template
        ("delya", POINTER(c_int_p)),
        ("narray", c_int),   # number of averaged templates
        ("size", c_int),   # size of count array (width of pixs)
        ("setwidth", c_int_p),   # setwidths for each template
        ("nasum", LPNuma),   # pixel count in pixs by column
        ("namoment", LPNuma),   # first moment of pixels in pixs by cols
        ("fullarrays", c_int),   # 1 if full arrays are made; 0 otherwise
        ("beta", c_float_p),   # channel coeffs for template fg term
        ("gamma", c_float_p),   # channel coeffs for bit-and term
        ("trellisscore", c_float_p),   # score on trellis
        # template on trellis (for backtrack)
        ("trellistempl", c_int_p),
        ("natempl", LPNuma),   # indices of best path templates
        ("naxloc", LPNuma),   # x locations of best path templates
        ("nadely", LPNuma),   # y locations of best path templates
        ("nawidth", LPNuma),   # widths of best path templates
        ("boxa", LPBoxa),   # Viterbi result for splitting input pixs
        ("nascore", LPNuma),   # correlation scores: best path templates
        ("natempl_r", LPNuma),   # indices of best rescored templates
        ("nasample_r", LPNuma),   # samples of best scored templates
        ("naxloc_r", LPNuma),   # x locations of best rescoredtemplates
        ("nadely_r", LPNuma),   # y locations of best rescoredtemplates
        ("nawidth_r", LPNuma),   # widths of best rescoredtemplates
        ("nascore_r", LPNuma)  # correlation scores: rescored templates
    ]


LPL_Rdid = POINTER(L_Rdid)
LPLPL_Rdid = POINTER(LPL_Rdid)


class L_Recog(Structure):
    _fields_ = [
        ("scalew", c_int),   # scale all examples to this width;
        ("scaleh", c_int),   # scale all examples to this height;
        ("linew", c_int),   # use a value > 0 to convert the bitmap
        ("templ_use", c_int),   # template use: use either the average
        ("maxarraysize", c_int),   # initialize container arrays to this
        ("setsize", c_int),   # size of character set
        ("threshold", c_int),   # for binarizing if depth > 1
        ("maxyshift", c_int),   # vertical jiggle on nominal centroid
        ("charset_type", c_int),   # one of L_ARABIC_NUMERALS, etc.
        # expected number of classes in charset
        ("charset_size", c_int),
        ("min_nopad", c_int),   # min number of samples without padding
        ("num_samples", c_int),   # number of training samples
        ("minwidth_u", c_int),   # min width averaged unscaled templates
        ("maxwidth_u", c_int),   # max width averaged unscaled templates
        ("minheight_u", c_int),   # min height averaged unscaled templates
        ("maxheight_u", c_int),   # max height averaged unscaled templates
        ("minwidth", c_int),   # min width averaged scaled templates
        ("maxwidth", c_int),   # max width averaged scaled templates
        ("ave_done", c_int),   # set to 1 when averaged bitmaps are made
        ("train_done", c_int),   # set to 1 when training is complete or
        ("max_wh_ratio", c_float),   # max width/height ratio to split
        # max of max/min template height ratio
        ("max_ht_ratio", c_float),
        ("min_splitw", c_int),   # min component width kept in splitting
        ("max_splith", c_int),   # max component height kept in splitting
        ("sa_text", LPSarray),   # text array for arbitrary char set
        # index-to-char lut for arbitrary charset
        ("dna_tochar", LPL_Dna),
        ("centtab", c_int_p),   # table for finding centroids
        ("sumtab", c_int_p),   # table for finding pixel sums
        ("pixaa_u", LPPixaa),   # all unscaled templates for each class
        ("ptaa_u", LPPtaa),   # centroids of all unscaled templates
        ("naasum_u", LPNumaa),   # area of all unscaled templates
        ("pixaa", LPPixaa),   # all (scaled) templates for each class
        ("ptaa", LPPtaa),   # centroids of all (scaledl) templates
        ("naasum", LPNumaa),   # area of all (scaled) templates
        ("pixa_u", LPPixa),   # averaged unscaled templates per class
        ("pta_u", LPPta),   # centroids of unscaled ave. templates
        ("nasum_u", LPNuma),   # area of unscaled averaged templates
        ("pixa", LPPixa),   # averaged (scaled) templates per class
        ("pta", LPPta),   # centroids of (scaled) ave. templates
        ("nasum", LPNuma),   # area of (scaled) averaged templates
        ("pixa_tr", LPPixa),   # all input training images
        ("pixadb_ave", LPPixa),   # unscaled and scaled averaged bitmaps
        ("pixa_id", LPPixa),   # input images for identifying
        # debug: best match of input against ave.
        ("pixdb_ave", LPPix),
        ("pixdb_range", LPPix),   # debug: best matches within range
        ("pixadb_boot", LPPixa),   # debug: bootstrap training results
        ("pixadb_split", LPPixa),   # debug: splitting results
        ("bmf", LPL_Bmf),   # bmf fonts
        ("bmf_size", c_int),   # font size of bmf; default is 6 pt
        ("did", LPL_Rdid),   # temp data used for image decoding
        ("rch", LPL_Rch),   # temp data used for holding best char
        ("rcha", LPL_Rcha)  # temp data used for array of best chars
    ]


LPL_Recog = POINTER(L_Recog)
LPLPL_Recog = POINTER(LPL_Recog)
