import multiprocessing

def fibon(n):
    if n < 2:
        return n 
    else:
        p1 = multiprocessing.Process(target=fibon, args=(n-1,))
        p1.start()
        p1.join()

        