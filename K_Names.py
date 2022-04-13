from json import tool
import perm_tools
import tools
from alphabet import alphabet
alphalength=len(alphabet)
def k_names(k):
    if(k<0):
        raise Exception()
    perms_built = 0
    num_of_perms = k
    perms = []
    if(tools.ktoolarge(k,alphalength)):
        print("K is too large ti manage with this alphabet")
        return

    while(num_of_perms>perms_built):
        char_index = tools.random_index(0,alphalength)
        seed = alphabet[char_index]
        len_of_perms = tools.random_index(4,alphalength)
        perms_per_seed = tools.random_index(1,alphalength)
        alphabet1=alphabet.replace(seed,"")
        newperms = perm_tools.perms_of_seed(seed,alphabet1,perms_per_seed,num_of_perms,len_of_perms,perms_built)
        perms += newperms
        perms_built += len(newperms)
    return perms
k_names(500)
