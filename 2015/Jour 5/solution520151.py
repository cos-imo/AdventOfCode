import sys, string, copy

def main():

    file=open('input','r')
    lst=file.readlines()

    res=0

    for line in lst:
        vowels="aeiou"
        double=0
        vowels_in_word=0
        for i in range(len(line)-1):
            double+=(line[i+1]==line[i])
            vowels_in_word+=(line[i] in vowels)
        vowels_in_word+=(line[-1] in vowels)
        res+=((vowels_in_word>2) and (not (("ab" in line) or ("cd" in line) or ("pq" in line) or ("xy" in line)) and double!=0))
    sys.stdout.write("{} strings are nice".format(str(res)))

if __name__=="__main__":
    main()