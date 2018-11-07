import time
from datetime import datetime, timedelta
from pyats.easypy import Task
import sys
import argparse

def main(runtime):
    parser = argparse.ArgumentParser(description='Parser for two numbers')
    parser.add_argument('-a', type = float, dest = 'a', default = 1, required = False, help = 'You must enter number for correct test')
    parser.add_argument('-b', type = float, dest = 'b', default = 1, required = False, help = 'You must enter number for correct test')
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:0])

    task_1 = Task(testscript ='add_func.py',
                  taskid = 'add_func_task',
                  runtime=runtime,
                  a = args.a, b = args.b)

    task_2 = Task(testscript = 'div_func.py',
                  taskid = 'div_func_task',
                  runtime=runtime,
                  a = args.a, b = args.b)

    task_3 = Task(testscript = 'mult_func.py',
                  taskid = 'mult_func_test',
                  runtime=runtime,
                  a = args.a, b = args.b)

    task_4 = Task(testscript = 'substract_func.py',
                  taskid = 'substract_func_py',
                  runtime=runtime,
                  a = args.a, b = args.b)

    task_1.start()
    task_2.start()
    task_3.start()
    task_4.start()
    all_t=[task_1, task_2, task_3, task_4]

    counter = timedelta(seconds=10)

    while counter:
        # check if processes are alive, if so, continue to wait
        if any(t.is_alive() for t in all_t):
            time.sleep(1)
            counter -= timedelta(seconds=1)
        else:
            break
    else:
        # exceeded runtime
        task_1.terminate()
        task_1.join()
        task_2.terminate()
        task_2.join()

        # raise exception
        raise TimeoutError('Not all tasks finished in 5 minutes!')