count = 0
data = []
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了,總共有',len(data),'筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
print('留言平均長度為: ', sum_len/len(data),'個字')

#篩選長度小於一百的留言

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('小於100的留言總共有: ', len(new), '筆留言')
print(new[0])
print(new[3])

# 篩選留言中有good的留言數

good = []
for d in data:
	if 'good' in d:
		good.append(len(data))
print ('有good的留言總共: ', len(good), '筆' )
print (good[0])