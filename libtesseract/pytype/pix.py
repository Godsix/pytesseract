from enum import IntEnum
from ctypes import (Structure, c_uint, c_int, c_void_p, c_ubyte, POINTER,
                    c_size_t, c_char_p)
from ..datatype import c_uint_p, c_float_p, c_double_p, c_ubyte_p


class RGBAColor(IntEnum):
    '''RGBA Color'''
    COLOR_RED = 0  # red color index in RGBA_QUAD
    COLOR_GREEN = 1  # green color index in RGBA_QUAD
    COLOR_BLUE = 2  # blue color index in RGBA_QUAD
    L_ALPHA_CHANNEL = 3  # alpha value index in RGBA_QUAD


class BoxColor(IntEnum):
    '''Box Color'''
    L_DRAW_RED = 0  # draw in red
    L_DRAW_GREEN = 1  # draw in green
    L_DRAW_BLUE = 2  # draw in blue
    L_DRAW_SPECIFIED = 3  # draw specified color
    L_DRAW_RGB = 4  # draw as sequence of r,g,b
    L_DRAW_RANDOM = 5  # draw randomly chosen colors


class CmapConversion(IntEnum):
    '''Cmap Conversion'''
    REMOVE_CMAP_TO_BINARY = 0  # remove colormap for conv to 1 bpp
    REMOVE_CMAP_TO_GRAYSCALE = 1  # remove colormap for conv to 8 bpp
    REMOVE_CMAP_TO_FULL_COLOR = 2  # remove colormap for conv to 32 bpp
    REMOVE_CMAP_WITH_ALPHA = 3  # remove colormap and alpha
    REMOVE_CMAP_BASED_ON_SRC = 4  # remove depending on src format


class ObjectAccess(IntEnum):
    '''Object Access'''
    L_NOCOPY = 0  # do not copy the object; do not delete the ptr
    L_INSERT = L_NOCOPY
    L_COPY = 1  # stuff it in; do not copy or clone
    L_CLONE = 2  # make/use a copy of the object
    L_COPY_CLONE = 3  # make/use clone (ref count) of the object


class SortMode(IntEnum):
    '''Sort Mode'''
    L_SHELL_SORT = 1  # use shell sort
    L_BIN_SORT = 2  # use bin sort


class SortOrder(IntEnum):
    '''Sort Order'''
    L_SORT_INCREASING = 1  # sort in increasing order
    L_SORT_DECREASING = 2  # sort in decreasing order


class SortType(IntEnum):
    '''Sort Type'''
    L_SORT_BY_X = 1  # sort box or c.c. by left edge location
    L_SORT_BY_Y = 2  # sort box or c.c. by top edge location
    L_SORT_BY_RIGHT = 3  # sort box or c.c. by right edge location
    L_SORT_BY_BOT = 4  # sort box or c.c. by bot edge location
    L_SORT_BY_WIDTH = 5  # sort box or c.c. by width
    L_SORT_BY_HEIGHT = 6  # sort box or c.c. by height
    L_SORT_BY_MIN_DIMENSION = 7  # sort box or c.c. by min dimension
    L_SORT_BY_MAX_DIMENSION = 8  # sort box or c.c. by max dimension
    L_SORT_BY_PERIMETER = 9  # sort box or c.c. by perimeter
    L_SORT_BY_AREA = 10  # sort box or c.c. by area
    L_SORT_BY_ASPECT_RATIO = 11  # sort box or c.c. by width/height ratio


class BlendTypes(IntEnum):
    '''Blend Types'''
    L_BLEND_WITH_INVERSE = 1  # add some of src inverse to itself
    L_BLEND_TO_WHITE = 2  # shift src colors towards white
    L_BLEND_TO_BLACK = 3  # shift src colors towards black
    L_BLEND_GRAY = 4  # blend src directly with blender
    L_BLEND_GRAY_WITH_INVERSE = 5  # add amount of src inverse to itself,


class PaintSelection(IntEnum):
    '''Paint Selection'''
    L_PAINT_LIGHT = 1  # colorize non-black pixels
    L_PAINT_DARK = 2  # colorize non-white pixels


class PixelSetting(IntEnum):
    '''Pixel Setting'''
    L_SET_PIXELS = 1  # set all bits in each pixel to 1
    L_CLEAR_PIXELS = 2  # set all bits in each pixel to 0
    L_FLIP_PIXELS = 3  # flip all bits in each pixel


class SizeComparison(IntEnum):
    '''Size Comparison'''
    L_SELECT_IF_LT = 1  # save if value is less than threshold
    L_SELECT_IF_GT = 2  # save if value is more than threshold
    L_SELECT_IF_LTE = 3  # save if value is <= to the threshold
    L_SELECT_IF_GTE = 4  # save if value is >= to the threshold


class SizeSelection(IntEnum):
    '''Size Selection'''
    L_SELECT_BY_WIDTH = 1  # select by width; 1 bpp
    L_SELECT_BY_HEIGHT = 2  # select by height; 1 bpp
    L_SELECT_BY_MAX_DIMENSION = 3  # select by max of width and
    L_SELECT_BY_AREA = 4  # select by foreground area; 1 bpp
    L_SELECT_BY_PERIMETER = 5  # select by perimeter; 1 bpp


class LocationFilter(IntEnum):
    '''Location Filter'''
    L_SELECT_WIDTH = 1  # width must satisfy constraint
    L_SELECT_HEIGHT = 2  # height must satisfy constraint
    L_SELECT_XVAL = 3  # x value must satisfy constraint
    L_SELECT_YVAL = 4  # y value must satisfy constraint
    L_SELECT_IF_EITHER = 5  # either width or height (or xval
    L_SELECT_IF_BOTH = 6  # both width and height (or xval


class BoxaCheck(IntEnum):
    '''Boxa Check'''
    L_CHECK_WIDTH = 1  # check and possibly modify width
    L_CHECK_HEIGHT = 2  # check and possibly modify height
    L_CHECK_BOTH = 3  # check and possibly modify both


class ColorSelection(IntEnum):
    '''Color Selection'''
    L_SELECT_RED = 1  # use red component
    L_SELECT_GREEN = 2  # use green component
    L_SELECT_BLUE = 3  # use blue component
    L_SELECT_MIN = 4  # use min color component
    L_SELECT_MAX = 5  # use max color component
    L_SELECT_AVERAGE = 6  # use average of color components
    L_SELECT_HUE = 7  # use hue value (in HSV color space)
    L_SELECT_SATURATION = 8  # use saturation value (in HSV space)
    L_SELECT_WEIGHTED = 9  # use weighted average of color comps


class ColorContent(IntEnum):
    '''Color Content'''
    L_INTERMED_DIFF = 1  # intermediate of diff component values
    L_AVE_MAX_DIFF_2 = 2  # diff average closest comps to third
    L_MAX_DIFF = 3  # maximum diff of component values


class Conversion16bit(IntEnum):
    '''16-bit Conversion'''
    L_LS_BYTE = 1  # use LSB
    L_MS_BYTE = 2  # use MSB
    L_AUTO_BYTE = 3  # use LSB if max(val) < 256; else MSB
    L_CLIP_TO_FF = 4  # use max(val, 255)
    L_LS_TWO_BYTES = 5  # use two LSB
    L_MS_TWO_BYTES = 6  # use two MSB
    L_CLIP_TO_FFFF = 7  # use max(val, 65535)


class RotationType(IntEnum):
    '''Rotation Type'''
    L_ROTATE_AREA_MAP = 1  # use area map rotation, if possible
    L_ROTATE_SHEAR = 2  # use shear rotation
    L_ROTATE_SAMPLING = 3  # use sampling


class BackgroundColor(IntEnum):
    '''Background Color'''
    L_BRING_IN_WHITE = 1  # bring in white pixels from the outside
    L_BRING_IN_BLACK = 2  # bring in black pixels from the outside


class ShearPoint(IntEnum):
    '''Shear Point'''
    L_SHEAR_ABOUT_CORNER = 1  # shear image about UL corner
    L_SHEAR_ABOUT_CENTER = 2  # shear image about center


class AffineTransformOrder(IntEnum):
    '''Affine Transform Order'''
    L_TR_SC_RO = 1  # translate, scale, rotate
    L_SC_RO_TR = 2  # scale, rotate, translate
    L_RO_TR_SC = 3  # rotate, translate, scale
    L_TR_RO_SC = 4  # translate, rotate, scale
    L_RO_SC_TR = 5  # rotate, scale, translate
    L_SC_TR_RO = 6  # scale, translate, rotate


class GrayscaleFill(IntEnum):
    '''Grayscale Fill'''
    L_FILL_WHITE = 1  # fill white pixels (e.g, in fg map)
    L_FILL_BLACK = 2  # fill black pixels (e.g., in bg map)


class BlackWhiteSet(IntEnum):
    '''BlackWhite Set'''
    L_SET_WHITE = 1  # set pixels to white
    L_SET_BLACK = 2  # set pixels to black


class BlackWhiteGet(IntEnum):
    '''BlackWhite Get'''
    L_GET_WHITE_VAL = 1  # get white pixel value
    L_GET_BLACK_VAL = 2  # get black pixel value


class BlackWhiteSum(IntEnum):
    '''BlackWhite Sum'''
    L_WHITE_IS_MAX = 1  # white pixels are 0xff or 0xffff; black are 0
    L_BLACK_IS_MAX = 2  # black pixels are 0xff or 0xffff; white are 0


class DitherDistance(IntEnum):
    '''Dither Distance'''
    DEFAULT_CLIP_LOWER_1 = 10  # dist to black with no prop; 1 bpp
    DEFAULT_CLIP_UPPER_1 = 10  # dist to black with no prop; 1 bpp
    DEFAULT_CLIP_LOWER_2 = 5  # dist to black with no prop; 2 bpp
    DEFAULT_CLIP_UPPER_2 = 5  # dist to black with no prop; 2 bpp


class DistanceType(IntEnum):
    '''Distance Type'''
    L_MANHATTAN_DISTANCE = 1  # L1 distance (e.g., in color space)
    L_EUCLIDEAN_DISTANCE = 2  # L2 distance


class DistanceValue(IntEnum):
    '''Distance Value'''
    L_NEGATIVE = 1  # values < 0
    L_NON_NEGATIVE = 2  # values >= 0
    L_POSITIVE = 3  # values > 0
    L_NON_POSITIVE = 4  # values <= 0
    L_ZERO = 5  # values = 0
    L_ALL = 6  # all values


class StatsType(IntEnum):
    '''Stats Type'''
    L_MEAN_ABSVAL = 1  # average of abs values
    L_MEDIAN_VAL = 2  # median value of set
    L_MODE_VAL = 3  # mode value of set
    L_MODE_COUNT = 4  # mode count of set
    L_ROOT_MEAN_SQUARE = 5  # rms of values
    L_STANDARD_DEVIATION = 6  # standard deviation from mean
    L_VARIANCE = 7  # variance of values


class IndexSelection(IntEnum):
    '''Index Selection'''
    L_CHOOSE_CONSECUTIVE = 1  # select 'n' consecutive
    L_CHOOSE_SKIP_BY = 2  # select at intervals of 'n'


class TextOrientation(IntEnum):
    '''Text Orientation'''
    L_TEXT_ORIENT_UNKNOWN = 0  # low confidence on text orientation
    L_TEXT_ORIENT_UP = 1  # portrait, text rightside-up
    L_TEXT_ORIENT_LEFT = 2  # landscape, text up to left
    L_TEXT_ORIENT_DOWN = 3  # portrait, text upside-down
    L_TEXT_ORIENT_RIGHT = 4  # landscape, text up to right


class EdgeOrientation(IntEnum):
    '''Edge Orientation'''
    L_HORIZONTAL_EDGES = 0  # filters for horizontal edges
    L_VERTICAL_EDGES = 1  # filters for vertical edges
    L_ALL_EDGES = 2  # filters for all edges


class LineOrientation(IntEnum):
    '''Line Orientation'''
    L_HORIZONTAL_LINE = 0  # horizontal line
    L_POS_SLOPE_LINE = 1  # 45 degree line with positive slope
    L_VERTICAL_LINE = 2  # vertical line
    L_NEG_SLOPE_LINE = 3  # 45 degree line with negative slope
    L_OBLIQUE_LINE = 4  # neither horizontal nor vertical


class ImageOrientation(IntEnum):
    '''Image Orientation'''
    L_PORTRAIT_MODE = 0  # typical: page is viewed with height > width
    L_LANDSCAPE_MODE = 1  # page is viewed at 90 deg to portrait mode


class ScanDirection(IntEnum):
    '''Scan Direction'''
    L_FROM_LEFT = 0  # scan from left
    L_FROM_RIGHT = 1  # scan from right
    L_FROM_TOP = 2  # scan from top
    L_FROM_BOT = 3  # scan from bottom
    L_SCAN_NEGATIVE = 4  # scan in negative direction
    L_SCAN_POSITIVE = 5  # scan in positive direction
    L_SCAN_BOTH = 6  # scan in both directions
    L_SCAN_HORIZONTAL = 7  # horizontal scan (direction unimportant)
    L_SCAN_VERTICAL = 8  # vertical scan (direction unimportant)


class BoxAdjustment(IntEnum):
    '''Box Adjustment'''
    L_ADJUST_SKIP = 0  # do not adjust
    L_ADJUST_LEFT = 1  # adjust left edge
    L_ADJUST_RIGHT = 2  # adjust right edge
    L_ADJUST_LEFT_AND_RIGHT = 3  # adjust both left and right edges
    L_ADJUST_TOP = 4  # adjust top edge
    L_ADJUST_BOT = 5  # adjust bottom edge
    L_ADJUST_TOP_AND_BOT = 6  # adjust both top and bottom edges
    L_ADJUST_CHOOSE_MIN = 7  # choose the min median value
    L_ADJUST_CHOOSE_MAX = 8  # choose the max median value
    L_SET_LEFT = 9  # set left side to a given value
    L_SET_RIGHT = 10  # set right side to a given value
    L_SET_TOP = 11  # set top side to a given value
    L_SET_BOT = 12  # set bottom side to a given value
    L_GET_LEFT = 13  # get left side location
    L_GET_RIGHT = 14  # get right side location
    L_GET_TOP = 15  # get top side location
    L_GET_BOT = 16  # get bottom side location


class BoxBoundaryMod(IntEnum):
    '''Box Boundary Mod'''
    L_USE_MINSIZE = 1  # use boundaries giving min size
    L_USE_MAXSIZE = 2  # use boundaries giving max size
    L_SUB_ON_LOC_DIFF = 3  # modify boundary if big location diff
    L_SUB_ON_SIZE_DIFF = 4  # modify boundary if big size diff
    L_USE_CAPPED_MIN = 5  # modify boundary with capped min
    L_USE_CAPPED_MAX = 6  # modify boundary with capped max


class BoxOverlapMod(IntEnum):
    '''Box Overlap Mod'''
    L_COMBINE = 1  # resize to bounding region; remove smaller
    L_REMOVE_SMALL = 2  # only remove smaller


class BoxCombineorSelect(IntEnum):
    '''Box Combine or Select'''
    L_GEOMETRIC_UNION = 1  # use union of two boxes
    L_GEOMETRIC_INTERSECTION = 2  # use intersection of two boxes
    L_LARGEST_AREA = 3  # use box with largest area
    L_SMALLEST_AREA = 4  # use box with smallest area


class BoxReplacement(IntEnum):
    '''Box Replacement'''
    L_USE_ALL_BOXES = 1  # consider all boxes in the sequence
    L_USE_SAME_PARITY_BOXES = 2  # consider boxes with the same parity


class BoxCornersandCenter(IntEnum):
    '''Box Corners and Center'''
    L_UPPER_LEFT = 1  # UL corner
    L_UPPER_RIGHT = 2  # UR corner
    L_LOWER_LEFT = 3  # LL corner
    L_LOWER_RIGHT = 4  # LR corner
    L_BOX_CENTER = 5  # center


class HorizWarpStretch(IntEnum):
    '''Horiz Warp Stretch'''
    L_WARP_TO_LEFT = 1  # increasing stretch or contraction to left
    L_WARP_TO_RIGHT = 2  # increasing stretch or contraction to right


class HorizWarpMode(IntEnum):
    '''Horiz Warp Mode'''
    L_LINEAR_WARP = 1  # stretch or contraction grows linearly
    L_QUADRATIC_WARP = 2  # stretch or contraction grows quadratically


class PixelSelection(IntEnum):
    '''Pixel Selection'''
    L_INTERPOLATED = 1  # linear interpolation from src pixels
    L_SAMPLED = 2  # nearest src pixel sampling only


class ThinningPolarity(IntEnum):
    '''Thinning Polarity'''
    L_THIN_FG = 1  # thin foreground of 1 bpp image
    L_THIN_BG = 2  # thin background of 1 bpp image


class RunlengthDirection(IntEnum):
    '''Runlength Direction'''
    L_HORIZONTAL_RUNS = 0  # determine runlengths of horizontal runs
    L_VERTICAL_RUNS = 1  # determine runlengths of vertical runs


class EdgeFilter(IntEnum):
    '''Edge Filter'''
    L_SOBEL_EDGE = 1  # Sobel edge filter
    L_TWO_SIDED_EDGE = 2  # Two-sided edge filter


class SubpixelColorOrder(IntEnum):
    '''Subpixel Color Order'''
    L_SUBPIXEL_ORDER_RGB = 1  # sensor order left-to-right RGB
    L_SUBPIXEL_ORDER_BGR = 2  # sensor order left-to-right BGR
    L_SUBPIXEL_ORDER_VRGB = 3  # sensor order top-to-bottom RGB
    L_SUBPIXEL_ORDER_VBGR = 4  # sensor order top-to-bottom BGR


class HSVHistogram(IntEnum):
    '''HSV Histogram'''
    L_HS_HISTO = 1  # Use hue-saturation histogram
    L_HV_HISTO = 2  # Use hue-value histogram
    L_SV_HISTO = 3  # Use saturation-value histogram


class HSVRegion(IntEnum):
    '''HSV Region'''
    L_INCLUDE_REGION = 1  # Use pixels with specified HSV region
    L_EXCLUDE_REGION = 2  # Use pixels outside HSV region


class AddTextLocation(IntEnum):
    '''Add Text Location'''
    L_ADD_ABOVE = 1  # Add text above the image
    L_ADD_BELOW = 2  # Add text below the image
    L_ADD_LEFT = 3  # Add text to the left of the image
    L_ADD_RIGHT = 4  # Add text to the right of the image
    L_ADD_AT_TOP = 5  # Add text over the top of the image
    L_ADD_AT_BOT = 6  # Add text over the bottom of the image
    L_ADD_AT_LEFT = 7  # Add text over left side of the image
    L_ADD_AT_RIGHT = 8  # Add text over right side of the image


class PixPlot(IntEnum):
    '''Pix Plot'''
    L_PLOT_AT_TOP = 1  # Plot horizontally at top
    L_PLOT_AT_MID_HORIZ = 2  # Plot horizontally at middle
    L_PLOT_AT_BOT = 3  # Plot horizontally at bottom
    L_PLOT_AT_LEFT = 4  # Plot vertically at left
    L_PLOT_AT_MID_VERT = 5  # Plot vertically at middle
    L_PLOT_AT_RIGHT = 6  # Plot vertically at right


class MaskGeneration(IntEnum):
    '''Mask Generation'''
    L_USE_INNER = 1  # Select the interior part
    L_USE_OUTER = 2  # Select the outer part (e.g., a frame)


class DisplayProgram(IntEnum):
    '''Display Program'''
    L_DISPLAY_WITH_XZGV = 1  # Use xzgv with pixDisplay()
    L_DISPLAY_WITH_XLI = 2  # Use xli with pixDisplay()
    L_DISPLAY_WITH_XV = 3  # Use xv with pixDisplay()
    L_DISPLAY_WITH_IV = 4  # Use irfvanview (win) with pixDisplay()
    L_DISPLAY_WITH_OPEN = 5  # Use open (apple) with pixDisplay()


class PixFlag(IntEnum):
    '''Flags used in Pix::special'''
    L_NO_CHROMA_SAMPLING_JPEG = 1  # Write full resolution chroma


class NegativeValue(IntEnum):
    '''Negative Value'''
    L_CLIP_TO_ZERO = 1  # Clip negative values to 0
    L_TAKE_ABSVAL = 2  # Convert to positive using L_ABS()


class RelativeToZero(IntEnum):
    '''Relative To Zero'''
    L_LESS_THAN_ZERO = 1  # Choose values less than zero
    L_EQUAL_TO_ZERO = 2  # Choose values equal to zero
    L_GREATER_THAN_ZERO = 3  # Choose values greater than zero


class TrailingSlash(IntEnum):
    '''Trailing Slash'''
    L_ADD_TRAIL_SLASH = 1  # Add trailing slash to string
    L_REMOVE_TRAIL_SLASH = 2  # Remove trailing slash from string


class PixColormap(Structure):
    '''Colormap of a Pix'''
    _fields_ = [("array", c_void_p),  # colormap table (array of RGBA_QUAD)
                ("depth", c_int),  # of pix (1, 2, 4 or 8 bpp)
                ("nalloc", c_int),  # number of color entries allocated
                ("n", c_int)]  # number of color entries used


LPPixColormap = POINTER(PixColormap)
LPLPPixColormap = POINTER(LPPixColormap)


class Pix(Structure):
    '''Basic Pix'''
    _fields_ = [("w", c_uint),  # width in pixels
                ("h", c_uint),  # height in pixels
                ("d", c_uint),  # depth in bits (bpp)
                ("spp", c_uint),  # number of samples per pixel
                ("wpl", c_uint),  # 32-bit words/line
                ("refcount", c_uint),  # reference count (1 if no clones)
                # image res (ppi) in x direction (use 0 if unknown)
                ("xres", c_int),
                # image res (ppi) in y direction (use 0 if unknown)
                ("yres", c_int),
                ("informat", c_int),  # input file format, IFF_*
                ("special", c_int),  # special instructions for I/O, etc
                ("text", c_char_p),  # text string associated with pix
                ("colormap", LPPixColormap),  # colormap (may be null)
                ("data", c_uint_p)]  # the image data


LPPix = POINTER(Pix)
LPLPPix = POINTER(LPPix)


class RGBA_Quad(Structure):
    '''
    Colormap table entry (after the BMP version).
    Note that the BMP format stores the colormap table exactly
    as it appears here, with color samples being stored sequentially,
    in the order (b,g,r,a).
    '''
    _fields_ = [("blue", c_ubyte),  # blue value
                ("green", c_ubyte),  # green value
                ("red", c_ubyte),  # red value
                ("alpha", c_ubyte)]  # alpha value


LPRGBA_Quad = POINTER(RGBA_Quad)
LPLPRGBA_Quad = POINTER(LPRGBA_Quad)


class Box(Structure):
    '''Basic rectangle'''
    _fields_ = [("x", c_int),  # left coordinate
                ("y", c_int),  # top coordinate
                ("w", c_int),  # box width
                ("h", c_int),  # box height
                ("refcount", c_uint)]  # reference count (1 if no clones)


LPBox = POINTER(Box)
LPLPBox = POINTER(LPBox)


class Boxa(Structure):
    '''Array of Box'''
    _fields_ = [("n", c_int),  # number of box in ptr array
                ("nalloc", c_int),  # number of box ptrs allocated
                ("refcount", c_uint),  # reference count (1 if no clones)
                ("box", LPLPBox)]  # box ptr array


LPBoxa = POINTER(Boxa)
LPLPBoxa = POINTER(LPBoxa)


class Boxaa(Structure):
    '''Array of Boxa'''
    _fields_ = [("n", c_int),  # number of boxa in ptr array
                ("nalloc", c_int),  # number of boxa ptrs allocated
                ("boxa", LPLPBoxa)]  # boxa ptr array


LPBoxaa = POINTER(Boxaa)
LPLPBoxaa = POINTER(LPBoxaa)


class Pixa(Structure):
    '''Array of pix'''
    _fields_ = [("n", c_int),  # number of Pix in ptr array
                ("nalloc", c_int),  # number of Pix ptrs allocated
                ("refcount", c_uint),  # reference count (1 if no clones)
                ("pix", LPLPPix),  # the array of ptrs to pix
                ("boxa", LPBoxa)]  # array of boxes


LPPixa = POINTER(Pixa)
LPLPPixa = POINTER(LPPixa)


class Pixaa(Structure):
    '''Array of arrays of pix'''
    _fields_ = [("n", c_int),  # number of Pixa in ptr array
                ("nalloc", c_int),  # number of Pixa ptrs allocated
                ("pixa", LPLPPixa),  # array of ptrs to pixa
                ("boxa", LPBoxa)]  # array of boxes


LPPixaa = POINTER(Pixaa)
LPLPPixaa = POINTER(LPPixaa)


class Pta(Structure):
    '''Array of points'''
    _fields_ = [("n", c_int),  # actual number of pts
                ("nalloc", c_int),  # size of allocated arrays
                ("refcount", c_uint),  # reference count (1 if no clones)
                ("x", c_float_p),  # arrays of floats
                ("y", c_float_p)]  # arrays of floats


LPPta = POINTER(Pta)
LPLPPta = POINTER(LPPta)


class Ptaa(Structure):
    '''Array of Pta'''
    _fields_ = [("n", c_int),  # number of pta in ptr array
                ("nalloc", c_int),  # number of pta ptrs allocated
                ("pta", LPLPPta)]  # pta ptr array


LPPtaa = POINTER(Ptaa)
LPLPPtaa = POINTER(LPPtaa)


class Pixacc(Structure):
    '''Pix accumulator container'''
    _fields_ = [("w", c_int),  # array width
                ("h", c_int),  # array height
                ("offset", c_int),  # used to allow negative
                ("pix", LPPix)]  # the 32 bit accumulator pix


LPPixacc = POINTER(Pixacc)
LPLPPixacc = POINTER(LPPixacc)


class PixTiling(Structure):
    '''Pix tiling'''
    _fields_ = [("pix", LPPix),  # input pix (a clone)
                ("nx", c_int),  # number of tiles horizontally
                ("ny", c_int),  # number of tiles vertically
                ("w", c_int),  # tile width
                ("h", c_int),  # tile height
                ("xoverlap", c_int),  # overlap on left and right
                ("yoverlap", c_int),  # overlap on top and bottom
                ("strip", c_int)]  # strip for paint; default is TRUE


LPPixTiling = POINTER(PixTiling)
LPLPPixTiling = POINTER(LPPixTiling)


class FPix(Structure):
    '''Pix with float array'''
    _fields_ = [("w", c_int),  # width in pixels
                ("h", c_int),  # height in pixels
                ("wpl", c_int),  # 32-bit words/line
                ("refcount", c_uint),  # reference count (1 if no clones)
                ("xres", c_int),  # image res (ppi) in x direction
                ("yres", c_int),  # image res (ppi) in y direction
                ("data", c_float_p)]  # the float image data


LPFPix = POINTER(FPix)
LPLPFPix = POINTER(LPFPix)


class FPixa(Structure):
    '''Array of FPix'''
    _fields_ = [("n", c_int),  # number of fpix in ptr array
                ("nalloc", c_int),  # number of fpix ptrs allocated
                ("refcount", c_uint),  # reference count (1 if no clones)
                ("fpix", LPLPFPix)]  # the array of ptrs to fpix


LPFPixa = POINTER(FPixa)
LPLPFPixa = POINTER(LPFPixa)


class DPix(Structure):
    '''Pix with double array'''
    _fields_ = [("w", c_int),  # width in pixels
                ("h", c_int),  # height in pixels
                ("wpl", c_int),  # 32-bit words/line
                ("refcount", c_uint),  # reference count (1 if no clones)
                ("xres", c_int),  # image res (ppi) in x direction
                ("yres", c_int),  # image res (ppi) in y direction
                ("data", c_double_p)]  # the double image data


LPDPix = POINTER(DPix)
LPLPDPix = POINTER(LPDPix)


class PixComp(Structure):
    '''Compressed Pix'''
    _fields_ = [("w", c_int),  # width in pixels
                ("h", c_int),  # height in pixels
                ("d", c_int),  # depth in bits
                ("xres", c_int),  # image res (ppi) in x direction
                ("yres", c_int),  # image res (ppi) in y direction
                ("comptype", c_int),  # compressed format (IFF_TIFF_G4,
                ("text", c_char_p),  # text string associated with pix
                ("cmapflag", c_int),  # flag (1 for cmap, 0 otherwise)
                ("data", c_ubyte_p),  # the compressed image data
                ("size", c_size_t)]  # size of the data array


LPPixComp = POINTER(PixComp)
LPLPPixComp = POINTER(LPPixComp)


class PixaComp(Structure):
    '''Array of compressed pix'''
    _fields_ = [("n", c_int),  # number of PixComp in ptr array
                ("nalloc", c_int),  # number of PixComp ptrs allocated
                ("offset", c_int),  # indexing offset into ptr array
                ("pixc", LPLPPixComp),  # the array of ptrs to PixComp
                ("boxa", LPBoxa)]  # array of boxes


LPPixaComp = POINTER(PixaComp)
LPLPPixaComp = POINTER(LPPixaComp)
