from ctypes import Structure, c_int, c_void_p, POINTER


class L_Stack(Structure):
    '''
    Expandable pointer stack for arbitrary void * data.
    Note that array[n] is the first null ptr in the array
    '''
    pass


LPL_Stack = POINTER(L_Stack)
LPLPL_Stack = POINTER(LPL_Stack)

L_Stack._fields_ = [
    ("nalloc", c_int),   # size of ptr array
    ("n", c_int),   # number of stored elements
    ("array", POINTER(c_void_p)),   # ptr array
    ("auxstack", LPL_Stack)  # auxiliary stack
]
