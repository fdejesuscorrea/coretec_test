import math
import random
def ktoolarge(k,alp_len):
    if(k>(alp_len**alp_len)):
        return True
    else:
        return False
    
def kltoolarge(k,l,alphalength):
    if(l>alphalength):
        return True
    perms = npr(alphalength,l)
    if((alphalength-l)<0):
        return True
    if(k>perms):
        return True
    else:
        return False
def npr(n,r):
    nfact = math.factorial(n)
    nminusr_fact = math.factorial(n-r)
    return nfact/nminusr_fact
def random_index(min,max): #i didn't wanted to import as less as possible in my main solution file so i added this indirection level.
    ranin = random.randint(min,max-1)
    return ranin