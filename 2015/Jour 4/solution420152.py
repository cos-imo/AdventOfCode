import hashlib, sys

def main():

    file=open('input','r')
    string=file.readlines()[0]
    
    proof_of_work=0

    while (hashlib.md5((string+str(proof_of_work)).encode()).hexdigest()[0:6]!="000000"):       # Nah, I mean, seriously...
        proof_of_work+=1
            
    sys.stdout.write("proof of work: " + str(proof_of_work))

if __name__=="__main__":
    main()