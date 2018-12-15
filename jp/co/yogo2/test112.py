
from memory_profiler import profile

@profile
def generate_nums():
    num = 0
    while True:
        yield num
        num = num + 1


nums = generate_nums()

#for x in nums:
#    print(x)
#
#    if x > 9:
#        break

print(list(map(lambda x:x,[next(nums) for i in range(100000000) ])))


