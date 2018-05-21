#from huff import HuffmanCoding
from movetofrontencode import mtfEncode
from movetofrontdecode import mtfdecode
from hfc import encode

from bwtnew import suffix_array,decompress

def main():
    f = open("test2.txt", "r", encoding="utf-8")
    content = f.readlines()
    #content = content[:(len(content)//2)]
    str_content = ''.join(content)
    #print(str_content)
    arr = suffix_array(str_content)
    #print(arr)
    bwt=""
    front=""
    print("d1")
    #frq to keep track of frequencies
    frq=[]
    count=-1
    prev=None
    #sorted character list
    sorted_char=[]

    #Finding out BWT through Suffix array
    for i in arr:
        bwt=bwt+i[-1]
        front=front+i[0]
        if prev==i[0]:
            frq[count][1]=frq[count][1]+1
        else:
            frq.append([i[0],1])
            sorted_char.append(i[0])
            count=count+1
        prev=i[0]
    print("bwt done")
    #print(frq)
    #print(sorted_char)
    # ------print("BWT is:")
    # ------print(bwt)
    # ------print("---------")
    #print(front)
    #print(bwt)
    #print(frq)
    #print(sorted_char)
    # ans=decompress(front,bwt,frq,sorted_char)
    # #print(ans)
    # ans=ans[::-1]
    # print(ans[:-1])

    inputword=list(bwt)
    dd=mtfEncode(inputword)
    print("mtfe done")
    #-------print(dd)

    # OUTPUT OF MTF  = dd LIST OF NOS
    forstring = ''
    for i in dd:
        forstring = forstring + " "+ str(i)


    # h =  HuffmanCoding(path)
    # output_path = h.compress()
    # h.decompress(output_path)
    data = forstring

    #print( "$$$$$$$$$$$$$" + data + "$$$$$$$$$$$$")

    huff = encode(data)
    #print(huff)
    huff_dict={}
    rev_dict={}
    for i in huff:
        huff_dict[i[0]]=i[1]
        rev_dict[i[1]]=i[0]

    #print(huff_dict)
    print("huffman done")
    flag=0

    print("Decompressed file: \n")

    iniString=""

    #Calculates Inistring that is string of huffman codes
    for i in data:
        j = huff_dict[i]
        for k in j:
            iniString = iniString + str(k)

    #li stores the integer value of binary numbers


    li=[]
    tempString=""
    # print(iniString)
    # print(len(iniString))
    for i in range(len(iniString)):
        if (len(tempString) < 8):

            tempString = tempString + iniString[i]
            #print(i,"if",tempString,end=" ")

        else:
            li.append(int(tempString,2))
            #print("else",tempString,int(tempString,2))
            #print(tempString)
            tempString = iniString[i]

    rest=tempString
    #print(rest)



    # BINARY WRITING CODE
    g=open("comp2.bin","w")
    g.write(rest)
    g.close()

    first=li[0]
    #print(li)
    f= open("comp.bin","wb")
    for i in li:

        f.write(i.to_bytes(1,byteorder="little"))
        #tempBinList=bin(ord(i.to_bytes(1, byteorder="little")))[2:]
        #print(len(bin(ord(i.to_bytes(1, byteorder="little")))[2:]))
        #while(len(tempBinList)<8):
         #   tempBinList="0"+tempBinList


    f.close()

    #print('')
    final=""
    list1=[]
    #final=bin(first)[2:]
    list1.append(first)
    with open("comp.bin", "rb") as f:
        byte = f.read(1)
        while byte != b"":
            # Do stuff with byte.
            byte = f.read(1)
            # byte_array.append(byte)
            try:
                  list1.append(ord(byte))
            except:
                pass


    #Rprint(list1)
    ans=""
    for i in list1:
        tempstr=bin(i)[2:]
        while(len(tempstr)<8):
            tempstr='0'+tempstr
        #print(tempstr,end="")
        ans=ans+tempstr

    g=open("comp2.bin","r")
    rest=g.read()
    g.close()
    ans=ans+rest
    # print(ans)
    #s is the code
    s=""
    answer=""



    for i in ans:
        s = s + i
        #print(s)
        try:
            answer=answer+rev_dict[s]
            #print(rev_dict[s])
            s=""
        except:
            pass

    # print(answer)

    ans = answer.split()
    for i in range(len(ans)):
        ans[i] = int(ans[i])


    # INPUT OF MTFDECODE = LIST FORM dd
    dd2=mtfdecode(ans)
    # print(dd2)

    ret_bwt = ''.join(dd2)
    ans=decompress(front,ret_bwt,frq,sorted_char)
    ans=ans[::-1]
    f.close()
    print(ans[:-1])

    # path = "daa/a.txt"
    #
    # h = HuffmanCoding(path)
    #
    # output_path = h.compress()
    # h.decompress(output_path)
if __name__ == "__main__":
    main()
