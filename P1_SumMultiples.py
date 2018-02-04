
def findMultsSimple(n, div_lst): #slow
    return sum([x for x in range(1,n) if (any([x%div == 0 for div in div_lst]))])

def findMultsCount(n, div_lst): #slightly faster
    def countBy(num):
        count, current = 0, 0
        while current < n:
            count += current
            current+=num
        return count
    return countBy(3) +  countBy(5) - countBy(15)   

def findMultsSummation(n, div_lst): #Fastest - uses summation formula (can do up to three, though this could be generalized) 
    if (len(div_lst) > 3):
        return "More than three elements"
    def max_index(divisor):
        ind = n/float(divisor)
        int_ind = int(ind)
        if (int_ind == ind):
            return ind-1.0
        else:
            return int(ind)
    sm_num = lambda divisor: divisor*max_index(divisor)*(max_index(divisor)+1)/2.0
    union = int(sum([sm_num(div) for div in div_lst]))
    if (len(div_lst) == 2):
        total_count = union - sm_num(div_lst[0]*div_lst[1])
    else:
        two_index_pairs = {sum([x,y]):(x,y) for x in range(0,3) for y in range(0,3) if x!=y}.values() #[(0,1), (0,2), (1,2)]
        two_set_sum = sum([ sm_num(div_lst[ind[0]]*div_lst[ind[1]]) for ind in two_index_pairs])
        total_count = union - two_set_sum + sm_num(reduce(lambda x,y: x*y, div_lst))
    return int(total_count)
    

"""
import cProfile, pstats, StringIO
pr = cProfile.Profile()
pr.enable()

#findMultsSummation()

pr.disable()
s = StringIO.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print s.getvalue()
"""
