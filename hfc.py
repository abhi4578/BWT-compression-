import heapq
from collections import defaultdict


def encode(data):
    frequency = defaultdict(int)
    for symbol in data:
        frequency[symbol] += 1
    heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

# h=open("test2.txt","r",encoding = 'utf-8')
# data2=h.readlines()
# data = "".join(data2)
# print(data)
#
# # data = "147 12 4 51 1 4 5 0 1 4 12 431 1 0 0 0 4 1 5 1 1"
# frequency = defaultdict(int)
# for symbol in data:
#     frequency[symbol] += 1
#
# huff = encode(data)
# print(huff)
# huff_dict={}
# rev_dict={}
# for i in huff:
#     huff_dict[i[0]]=i[1]
#     rev_dict[i[1]]=i[0]
#
# print(huff_dict)
#
# flag=0
#
# iniString=""
#
# #Calculates Inistring that is string of huffman codes
# for i in data:
#     j = huff_dict[i]
#     for k in j:
#         iniString = iniString + str(k)
#
# #li stores the integer value of binary numbers
# li=[]
# tempString=""
# print(iniString)
# print(len(iniString))
# for i in range(len(iniString)):
#     if (len(tempString) < 8):
#
#         tempString = tempString + iniString[i]
#         #print(i,"if",tempString,end=" ")
#
#     else:
#         li.append(int(tempString,2))
#         #print("else",tempString,int(tempString,2))
#         print(tempString)
#         tempString = iniString[i];
#
# rest=tempString
# print(rest)
# g=open("comp2.bin","w")
# g.write(rest)
# g.close()
#
# first=li[0]
# print(li)
# f= open("comp.bin","wb")
# for i in li:
#
#     f.write(i.to_bytes(1,byteorder="little"))
#     tempBinList=bin(ord(i.to_bytes(1, byteorder="little")))[2:]
#     #print(len(bin(ord(i.to_bytes(1, byteorder="little")))[2:]))
#     while(len(tempBinList)<8):
#         tempBinList="0"+tempBinList
#
#
#
# f.close()
#
# #print('')
# final=""
# list1=[]
# #final=bin(first)[2:]
# list1.append(first)
# with open("comp.bin", "rb") as f:
#     byte = f.read(1)
#     while byte != b"":
#         # Do stuff with byte.
#         byte = f.read(1)
#         # byte_array.append(byte)
#         try:
#               list1.append(ord(byte))
#         except:
#             pass
#
#
# #print(list1)
# ans=""
# for i in list1:
#     tempstr=bin(i)[2:]
#     while(len(tempstr)<8):
#         tempstr='0'+tempstr
#     #print(tempstr,end="")
#     ans=ans+tempstr
#
# g=open("comp2.bin","r")
# rest=g.read()
# g.close()
# ans=ans+rest
# print(ans)
# #s is the code
# s=""
# answer=""
#
#
#
# for i in ans:
#     s = s + i
#     #print(s)
#     try:
#         answer=answer+rev_dict[s]
#         #print(rev_dict[s])
#         s=""
#     except:
#         pass
#
# print(answer)
