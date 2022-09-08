from ctypes import Structure, POINTER, c_void_p


class DoubleLinkedList(Structure):
    pass


LPDoubleLinkedList = POINTER(DoubleLinkedList)
LPLPDoubleLinkedList = POINTER(LPDoubleLinkedList)

DoubleLinkedList._fields_ = [
    ("prev", LPDoubleLinkedList),
    ("next", LPDoubleLinkedList),
    ("data", c_void_p)
]
