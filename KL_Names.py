from perm_tools import perms_of_seed
import tools
from alphabet import alphabet
alphalength=len(alphabet)
def kl_names(k,l):
    perms=[]
    if(tools.kltoolarge(k,l,alphalength)):
       print("either K or l are too large o too small")
       return 
    global len_of_perms
    len_of_perms=l
    alph=alphabet
    global num_of_perms
    num_of_perms=k
    global perms_built
    perms_built=0
    perms_per_seed=tools.npr(alphalength-1,l-1)
    while(perms_built<k):
        alp_len=len(alph)
        char_index = tools.random_index(0,alp_len)
        char = alph[char_index]
        alph=alph.replace(char,"")
        alphabet1=alphabet.replace(char,"")
        newperms=perms_of_seed(char,alphabet1,perms_per_seed,num_of_perms,len_of_perms,perms_built)
        perms += newperms
        lenperms=len(perms)
        perms_built=lenperms
    return perms
kl_names(100,3)