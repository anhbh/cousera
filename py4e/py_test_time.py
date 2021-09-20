
import time

stat1=dict()
stat2=dict()
#numbers_sizes = (i*10**exp for exp in range(4, 8, 1) for i in range(1, 11, 5))
numbers_sizes = [10**exp for exp in range(4, 10, 1)]

print(str(numbers_sizes))

for input in numbers_sizes:
	# prog 1
	start_time=time.time()
	cube_numbers=[]
	for n in range(0,input):
		if n % 2 == 1:
            cube_numbers.append(n**3)
    process_time=time.time()-start_time
    print('Process1 time for', input, '\tis', time.time()-start_time)
    stat1[str(input)]=process_time

    # prog 2
    cube_numbers=[]
    start_time=time.time()
    
    cube_numbers = [n**3 for n in range(0,input) if n%2 == 1]

    process_time=time.time()-start_time
    print('Process2 time for', input, '\tis', time.time()-start_time)
    stat2[str(input)]=process_time

for i in numbers_sizes:
    print('Input:',i,'\t',stat1[i],'\t', stat2[i],'\t', stat2[i]-stat1[i])
