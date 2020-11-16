import os
import io

chunk_size=2024

with open('blbec.jpg', 'rb') as sf:
    act_chunk = sf.read(chunk_size)
    with open('druhej_blbec', 'wb') as df:
        while len(act_chunk) > 0:
            df.write(act_chunk)
            act_chunk = sf.read(chunk_size)

        sf.close()
        df.close()
