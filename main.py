########### Python 2.7 #############
# Parallel Execution
import os, time
from multiprocessing import Pool

print 'main.py Start'

def exec10():
	return os.system('G:\\FRTB\\IMA\\batch\\runES10.cmd')

def exec20():
	return os.system('G:\\FRTB\\IMA\\batch\\runES20.cmd')

def exec40():
	return os.system('G:\\FRTB\\IMA\\batch\\runES40.cmd')

def exec60():
	return os.system('G:\\FRTB\\IMA\\batch\\runES60.cmd')

def exec120():
	return os.system('G:\\FRTB\\IMA\\batch\\runES120.cmd')

if __name__ == '__main__':
	pool = Pool(processes=8)              # start worker processes
	result10 = pool.apply_async(exec10)
	result20 = pool.apply_async(exec20)
	result40 = pool.apply_async(exec40)
	result60 = pool.apply_async(exec60)
	result120 = pool.apply_async(exec120)
	
	print result10.get()          
	print result20.get()          
	print result40.get()          
	print result60.get()          
	print result120.get()          
	
print 'main.py Done'