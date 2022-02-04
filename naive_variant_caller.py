from collections import Counter
"""
Implement a naive variant caller.

Given a reference sequence and a read pileup, make one of the following variant calls at each position in the reference:
1. "nocall": not enough evidence to make a call
2. "ref": only the reference allele is present
3. "[ACGT]hom: an Alt allele (A,C,G, or T) is present in >75% of reads
4. "[ACGT]het: an Alt allele (A,C,G, or T) is present in 25%--75% of reads
5. "[ACGT]low: an Alt allele (A,C,G, or T) is present in <25% of reads

If more than 1 Alt allele is present, the variant call should contain all of them, comma delimited

For this exercise we are only considering SNVs

The call_variants function takes a min_depth argument; if the total read depth is less than this,
the position is "nocall"

Pileup notation:
"." or "," : Aligned base matches the ref allele at this position (+ or - strand)
[ACGT] or [acgt] : Aligned base is a mismatch to the reference (+ or - strand)
For this exercise, we are not considering strand information, so treat uppercase and lowercase equally.

IMPORTANT NOTE: the test_pileup data structure is a *pileup*: each string in the list is the set of
aligned bases at one position on the reference.  For example, the first string is only '.' and ',',
so at the first reference position (which is base 'T'), the pileup of aligned bases contains
only T base calls.
"""

test_ref = 'TTTAGAGCGC'
test_pileup = ['....,...,,,,.,...,',
          ',..,,,.c..C.,,,',
          'AAaAAaaaA.,AaaaAa',
          '.C.,.g,gG.G...,G.',
          '..,C,..C,,CCCC.C,c',
          '.,..tT,,.t',
          '',
          '.Taat..,.,...,',
          '.cc',
          'aA.,,A.,...,a.,Aa...,']


def call_variants(pileup, ref, min_depth):
    # TODO: Make a variant call at each position on ref, using the pileup
    call_set =[]
    ref_list = [x for x in ref]

    for i in range(len(ref)):
        tmp_list =[]
        vaf_dict = {"A": [], "T": [], "G": [], "C": []}  # initialize a dict for storing VAF values and key
        calls = [x.upper() for x in pileup[i]]
        #print(calls)
        read_depth = len(calls)
        if read_depth<min_depth or read_depth==0:
            tmp_list.append("At position " + str(i+1) +": The reference is " + ref[i] + ". No variant call available: not enough evidence to make a call.")
            i+=1
        else:
            d = Counter(calls)
            A_call = d["A"]/read_depth
            vaf_dict["A"].append(A_call)
            T_call = d["T"]/read_depth
            vaf_dict["T"].append(T_call)
            C_call = d["C"]/read_depth
            vaf_dict["C"].append(C_call)
            G_call = d["G"]/read_depth
            vaf_dict["G"].append(G_call)
            Normal_call = (d["."] + d[","])/read_depth
            if Normal_call == 1:
                tmp_list.append("At position " + str(i+1) +": The reference is " + ref[i] + ". Reference Called: Only the reference allele is present")
            for value in vaf_dict:
                if (vaf_dict[value][0]) > 0.75:
                    tmp_list.append("At position " + str(i+1) +": The reference is " + ref[
                        i] + ". " + value + " hom: an Alt allele "+ str(value)+" is present in >75% of reads.")
                    # base_list.append(vaf_dict)
                if (vaf_dict[value][0]) >= 0.25 and (vaf_dict[value][0]) <= 0.75:
                    tmp_list.append("At position " + str(i+1) +": The reference is " + ref[
                        i] + ". " + value + " het: an Alt allele "+ str(value)+" is present in 25%--75% of reads.")
                    # base_list.append(vaf_dict)
                if (vaf_dict[value][0]) < 0.25 and (vaf_dict[value][0]) != 0:
                    tmp_list.append("At position " + str(i+1) +": The reference is " + ref[
                        i] + ". " + value + " low: an Alt allele "+ str(value)+" is present in <25% of reads.")




        if len(tmp_list)!=0:
            if len(tmp_list) > 1:
                tmp_var = ", ".join(tmp_list)
                call_set.append(tmp_var)
            call_set.append(tmp_list[0])


    return call_set



def main():
    # Keep this line:
    call_set = call_variants(test_pileup, test_ref, 5)
    [print(w) for w in call_set]


    # TODO: print the ref positions (1-10), and the variant call at each position
    # (Bonus: can you use list comprehension to print the results with one line of code?)

if __name__ == '__main__':
    main()