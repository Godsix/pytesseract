from enum import IntEnum
from ctypes import (Structure, Union, POINTER, c_longlong, c_ulonglong,
                    c_double, c_void_p, c_int)


class RBTreeKeyType(IntEnum):
    '''RBTree Key Type'''
    L_INT_TYPE = 1
    L_UINT_TYPE = 2
    L_FLOAT_TYPE = 3


class Rb_Type(Union):
    '''
     Storage for keys and values for red-black trees, maps and sets.

     Note:
       (1) Keys and values of the valid key types are all 64-bit
       (2) (void *) can be used for values but not for keys.

    '''
    _fields_ = [
        ("itype", c_longlong),
        ("utype", c_ulonglong),
        ("ftype", c_double),
        ("ptype", c_void_p)
    ]


LPRb_Type = POINTER(Rb_Type)
LPLPRb_Type = POINTER(LPRb_Type)


class L_Rbtree_Node(Structure):
    pass


LPL_Rbtree_Node = POINTER(L_Rbtree_Node)
LPLPL_Rbtree_Node = POINTER(LPL_Rbtree_Node)

L_Rbtree_Node_fields_ = [
    ("key", Rb_Type),
    ("value", Rb_Type),
    ("left", LPL_Rbtree_Node),
    ("right", LPL_Rbtree_Node),
    ("parent", LPL_Rbtree_Node),
    ("color", c_int)
]


class L_Rbtree(Structure):
    _fields_ = [
        ("root", LPL_Rbtree_Node),
        ("keytype", c_int)
    ]


LPL_Rbtree = POINTER(L_Rbtree)
LPLPL_Rbtree = POINTER(LPL_Rbtree)
