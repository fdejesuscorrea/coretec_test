from tools import random_index
def getPermutation(alphabet,act_perm,len_of_perms):
    alph=alphabet
    alp_len=len(alph)
    act_len = len(act_perm)
    char_index = random_index(0,alp_len)
    char = alph[char_index]
    act_perm+=char
    alph=alph.replace(char,"")
    act_len+=1
    if(act_len==len_of_perms):
        return act_perm
    return getPermutation(alph,act_perm,len_of_perms)

def perms_of_seed(seed,alphabet,perms_per_seed,num_of_perms,len_of_perms,perms_built):
    ret = []
    this_seed=0
    pb= perms_built
    while(this_seed<perms_per_seed):
        if(pb==num_of_perms):
            return ret
        perm = getPermutation(alphabet,seed,len_of_perms)
        if perm not in ret:
            ret.append(perm)
            this_seed+=1
            pb+=1
        else:
            continue
    return ret