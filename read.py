data = []
count = 0
with open ('reviews.txt','r') as f:
	for line in f :
		data.append(line)
		count +=1
		if count % 1000 ==0:
			print(len(data))

sum = 0
for d in data :
	sum = sum +len(d)
print ('留言的平均長度是',sum/len(data))


new = []
for d in data:
	if  len(d) < 100:
		new.append(d)
print('總共有',len(new),'筆資料小於100字元')

		