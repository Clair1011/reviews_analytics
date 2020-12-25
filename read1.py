# 讀取留言
def read_file():
	count = 0
	data = []
	with open('reviews.txt','r') as f:
		for line in f:
			data.append(line)
			count += 1
			if count % 10000 == 0:
				print(len(data))
	return data
#文字計數
def word_count(data):
	wc ={} # word_count
	for d in data:
		words = d.split(' ') #將words 分割成清單
		# 建立字典 key(word) , value(次數)
		for word in words: 
			if word in wc:
				wc[word] +=1
			else:
				wc[word] = 1
		#print(wc)
		
	#將字典美化一行一行印出
	for word in wc:
		if wc[word] > 1000: 
			print(word, wc[word]) # key, value

	print(len(wc))
	print((wc['Clair'])) # 印出出現Clair出現的次數

	#讓使用者輸入要查找的字，並輸出次數
	while True:
		word = input("請輸入要查找的字: ")
		if word == 'q':
			break
		elif word not in wc:
			print('字典沒有該字喔~')
		else:
			print(word, "出現的次數為: ", wc[word])
	print('感謝使用本查詢功能~')

#留言平均長度
def sum_len():
	sum_len = 0
	for d in data:
		sum_len += len(d)
	print('留言平均長度為: ', sum_len/len(data),'個字')
#篩選長度小於一百的留言
def len_100():
	new = []
	for d in data:
		if len(d) < 100:
			new.append(d)
	print('小於100的留言總共有: ', len(new), '筆留言')
	print(new[0])
	print(new[3])

# 篩選留言中有good的留言數
def good():
	good = []
	for d in data:
		if 'good' in d:
			good.append(len(data))
	print ('有good的留言總共: ', len(good), '筆' )
	print (good[0])

def main():
	data = read_file()
	word_count(data)

main()
