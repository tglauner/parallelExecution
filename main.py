########### Python 2.7 #############
# Parallel Execution
import os, time
from multiprocessing import Pool

print 'main.py Start'

def exec1():
	os.system('process1.cmd')
	time.sleep(5)
	return 0
def exec2():
	os.system('process2.cmd')
	return 0
def exec3():
	os.system('process3.cmd')

if __name__ == '__main__':
	time.sleep(1)
	pool = Pool(processes=4)              # start 4 worker processes
	time.sleep(1)
	result1 = pool.apply_async(exec1)
	result2 = pool.apply_async(exec2)
	
	print result1.get(timeout=10)           # prints "100" unless your computer is *very* slow
	print result2.get(timeout=10)           # prints "100" unless your computer is *very* slow
	
print 'main.py Done'