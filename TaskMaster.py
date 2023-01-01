"""
While writing some code, you ran into a problem. Your code runs
very slowly, because you need to run many functions.
You do a bit of troubleshooting and notice that
you are not draining your system's resources.
Write a function that, given a list of "slow" functions,
will return the sum of the results without
waiting for each function to complete individually
"""

from threading import Thread


def task_master(funcList):
    results = []
    threads = []
    
    for func in funcList:
        fThread = Thread(target=lambda: results.append(func()))
        fThread.start()
        threads.append(fThread)
        
    for t in threads:
        t.join()
        
    return sum(results)