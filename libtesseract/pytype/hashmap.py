from enum import IntEnum
from ctypes import Structure, c_int, POINTER, c_ulonglong


class HashmapLookup(IntEnum):
    '''Hashmap Lookup'''
    L_UNDEFINED = 0  # invalid operation
    L_HMAP_CHECK = 1  # check if this key/val has been stored
    L_HMAP_CREATE = 2  # create and store a hashitem if not found


class L_Hashitem(Structure):
    '''
    Hash item, containing storage for the key, value and count.  The key
    is a l_uint64, which is hashed by the mod function to find the index
    into the hashtab.
    '''
    pass


LPL_Hashitem = POINTER(L_Hashitem)
LPLPL_Hashitem = POINTER(LPL_Hashitem)


L_Hashitem._fields_ = [
    ("key", c_ulonglong),   # key is hashed into index into hashtab
    ("val", c_ulonglong),   # number stored associated with the key
    ("count", c_int),   # number of elements seen with this key
    ("next", LPL_Hashitem)  # ptr to the next in the list
]


class L_Hashmap(Structure):
    '''General hash map'''
    _fields_ = [
        ("nitems", c_int),   # number of stored items
        ("ntogo", c_int),   # number of items to be stored
        ("maxocc", c_int),   # max average occupancy allowed
        ("hashtab", LPLPL_Hashitem),   # array of hash item ptrs
        ("tabsize", c_int)  # size of array of hash item ptrs
    ]


LPL_Hashmap = POINTER(L_Hashmap)
LPLPL_Hashmap = POINTER(LPL_Hashmap)
