def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bits(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    result=""
    for i in matrix:
        for j in i:
            binrappresentation='{0:08b}'.format(j)
            result+=binrappresentation
    return result

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    result=""
    for i in matrix:
        for j in i:
            binrappresentation='{0:c}'.format(j)
            result+=binrappresentation
    return result

matrix = [[99, 114, 121, 112], [116, 111, 123, 108], [49, 110, 51, 52], [114, 108, 121, 125]]


print(matrix2bytes(matrix))
