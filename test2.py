import time
import multiprocessing as mp
import random

l = list()

def process(rows):
    print(rows,"going to sleep")
    # time.sleep()
    return rows[0]
    # do all the processing


if __name__ == '__main__':
    pool = mp.Pool(10) # N > 1
    chunks = [[1,2,3,4,5,6],[7,8,9,6,5,4]]
    for rows in chunks:
        print(rows)
        r = pool.apply_async(process, rows)
        r.wait(None)

        print(r.successful())
        # print(r.wait(None))


    pool.close()
    pool.join()

    # print(l[0].successful())
    # for i in range(len(l)):
    #     print(l[i].get())

