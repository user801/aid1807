
# 練習:
  # 1.已知有列表
    # L = [3, 5]
    # 用索引和切片操作，將列表改為:
    # L = [1,2,3,4,5,6]
    # 將列表反轉(前後對調), 然後刪除最後一個元素
    # print(L) # [6,5,4,3,2]


# L = [3, 5]    # len=最後一個的下一個
# L[1:1] = [4]
# L[0:0] = [1,2]
# L[len(L):len(L)] = [6]
# print(L)

# L[:] = L[::-1]  #反轉
# del L[-1]
# print(L)


# 2. 寫程序，讓用戶循環輸入一些整數，當輸入-1時結束輸入，將這些整數存於列表L中
    # 1 打印您共輸入了幾個有效的數?
    # 2 打印您輸入的數的最大數是多少?
    # 3 打印您輸入的數的最小數是多少?
    # 4 打印您輸入這些數的平均值


# L = []  # 先創建一個列表,用來存儲輸入的整數
# while True:
	# n = int(input("請輸入(-1結束):"))
	# if n == -1:
		# break
	# L += [n]  # 將n追加到L列表中

# print(L)
# print("您輸入的有效數是:", len(L))
# print("您輸入的最大數是:", max(L))
# print("您輸入的最小數是:", min(L))
# print("您輸入的平均數是:", sum(L)/len(L))

# 練習:
  # 寫一個程序，輸入多行文字，當輸入空行時結束輸入
  # 將原輸入的所有字符串存於列表L中
  # 1. 按原來輸入的行的順序反向打印這些行
     # 列:
       # 輸入:hello world
       # 輸入:welcome to china
       # 輸入:I like python
       # 輸入: <回車>
     # 顯示
       # I like python
       # welcome to china
       # hello world
  # 2. 打印出您共輸入了多少文字符?

# L = []
# while True:
	# s = input("輸入: ")
	# if not s:
		# break
	# L.append(s)  #追加到L中

# print(L)

# s = 0  #用來紀錄字符個數
# i = len(L) -1   #得到最後一個行的索引
# while i >= 0:
	# print(L[i])
	# s += len(L[i])
	# i -= 1

# print("字符的個數是: ", s)


# s = "ABC"
# s2 = "123"
# L = [x + y for x in s for y in s2]
# print(L)

# ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

# L = [1, 3, 2, 1, 6, 4, 2, 98, 82]

# L2 = []
# for x in L:
	# 如果x 不在Ｌ２內，將其放入Ｌ２中
	# if x not in L2:
		# L2.append(x)
# print(L2)

# [1, 3, 2, 6, 4, 98, 82]










