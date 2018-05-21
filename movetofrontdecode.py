def mtfdecode(wordcode):

	alphalist = []  # contains all unicode chararcters in form of lookup table
	for i in range(65535):
		alphalist.append(chr(i))
	outputarr=[]
	for i in range(len(wordcode)):
		outputarr.append(alphalist[wordcode[i]])
		del alphalist[wordcode[i]]
		alphalist.insert(0,outputarr[i])
	return outputarr	


