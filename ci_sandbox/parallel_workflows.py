import numpy as np



def read_chunk(array_size: int, ichunk: int,  callable=None):
    if callable is None:
        return np.random.random((array_size,))
    else:
        return callable(array_size, ichunk)


def serial_read(nchunks: int, chunksize: int, callable=None):
    chunkdata = []
    for ichunk in range(nchunks):
        chunkdata.append(read_chunk(chunksize, ichunk, callable=callable))
    return np.concatenate(chunkdata, axis=0)







