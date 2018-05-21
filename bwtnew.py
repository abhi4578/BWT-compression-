import string

def suffix_array(input_list):
	suffix_arr=[]
	input_list=input_list+chr(9)
	for i in range(len(input_list)):
		st1=input_list[-i:]
		st2=input_list[:-i]
		#print(st1+st2)
		suffix_arr.append(st1+st2)
	
	suffix_arr.sort()	
	return suffix_arr

def decompress(front,back,frq,sorted_char):
	final=""
	currentIndex=0
	final=final+front[currentIndex]
	final=final+back[currentIndex]
	
	dict={}
	char_count={}
	front_sub=[]
	back_sub=[]
	j=0
	for i in sorted_char:
		dict[i]=0
		char_count[i]=frq[j][1]
		j=j+1

	for i in range(len(front)):
		front_sub.append(front[:i].count(front[i]))

	for i in range(len(back)):
		back_sub.append(back[:i].count(back[i]))

	# print("-----------------")
	# print(front_sub)	
	# print(back_sub)
	# print(dict)
	# print(front)
	# print(back)
	# print(frq)
	# print(char_count)

	while len(final)<len(back):
			indSub=back_sub[currentIndex]
			#print("IndSub",indSub)
			ind=front.index(final[-1])
			#print("ind",ind)
			finalInd=ind+indSub
			final=final+back[finalInd]
			currentIndex=finalInd
			# ind=sorted_char.index(final[-1])
			# finalInd=0
			# for i in range(0,ind):
			# 	finalInd=finalInd + frq[i][1]

			# print(finalInd)	
			# ind1 = dict[final[-1]]
			# dict[final[-1]] = dict[final[-1]] + 1
			# print(finalInd,dict[final[-1]],back[finalInd])
			# final=final+back[finalInd+ind1]

	return final		

# print("Enter the String")
# arr=input()


