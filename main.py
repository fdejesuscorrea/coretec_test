from K_Names import k_names
from KL_Names import kl_names
def main():
    exit=False
    while(not exit):
        print("Please write the number (without parenthesis) whose algorithm you would like to test or type 'exit' to finish test")
        print("(1) K_names")
        print("(1.1) K_names info")
        print("(2) KL_Names")
        print("(2.1) KL_Names info")
        sel=input()
        if(sel=="1"):
            print("please insert the value for K")
            k=input()
            try:
                k=int(k)
            except(ValueError):
                print("-------__________----------______")
                print("you should only type numerical inputs")
                print("-------__________----------______")
                continue
            try:
                names=k_names(k)
            except:
                print("-------__________----------______")
                print("that value doesn't fits this algorithm")
                print("-------__________----------______")
                continue
            print("-------__________----------______")
            print(names)
            print("-------__________----------______")
            print("the number of names desired was: ",k)
            print("the number of names generated was: ",len(names))
            print("if this statement is true, you can be sure each name is unique")
            print("-------__________----------______")
            print(len(names)==len(set(names)))
            print("-------__________----------______")
            print("the proof of uniqueness for each character in each name is left as an exercise to the reader")
            print("i am pretty sure this algorithm fulfills it, though :p")
        else:
            if(sel=="1.1"):
                print("____________________________________________----------------------------------------_________________________________")
                print("The K_Names algorithm is the one that generates K diferent, variable length strings in which no character from the alphabet is repeated")
                print("____________________________________________----------------------------------------_________________________________")
            else:
                if(sel=="2"):
                    print("please insert the value for K and  L separated by a blank space with l > 2 and k>=0")
                    params = input().split(" ")
                    if(len(params)!=2):
                        print("-------__________----------______")
                        print("please type exactly two parameters")
                        print("-------__________----------______")
                        continue
                    k=params[0]
                    l=params[1]
                    try:
                        k=int(k)
                        l=int(l)
                    except:
                        print("-------__________----------______")
                        print("please type only numerical values for k an l")
                        print("-------__________----------______")
                        continue
                    try:
                        names = kl_names(k,l)
                    except:
                        print("those values are not fit for this algorithm")
                        continue
                    print(names)
                    print("the number of names desired was: ",k)
                    print("the length desired was: ",l)
                    print("the number of names generated was: ",len(names))
                    print("if this statement is true, you can be sure each name is unique")
                    print("-------__________----------______")
                    print(len(names)==len(set(names)))
                    print("-------__________----------______")
                    print("the proof of uniqueness for each character in each name is left as an exercise to the reader")
                    print("i am pretty sure this algorithm fulfills it, though :p")
                else:
                            if(sel=="2.1"):
                                print("____________________________________________----------------------------------------_________________________________")
                                print("The KL_Names algorithm is the one that generates K diferent, fixed length (L) strings in which no character from the alphabet is repeated")
                                print("____________________________________________----------------------------------------_________________________________")
                            else:
                                        if(sel=="2.1"):
                                            print("____________________________________________----------------------------------------_________________________________")
                                            print("The KL_Names algorithm is the one that generates K diferent, fixed length (L) strings in which no character from the alphabet is repeated")
                                            print("____________________________________________----------------------------------------_________________________________")
                                        else:
                                            if(sel=="exit"):
                                                exit=True
                                            else:
                                                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                                print("type a valid option's number")
                                                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        

main()