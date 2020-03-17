

# s = "ABCDE"
# for ch in s:
	# print("ch -->", ch)   # 重複執行   ch 綁定 A B C D E  
# else:
	# print("for 語句執行else子句")

# print("程序退出")

#上面跑出的程式
# ch --> A
# ch --> B
# ch --> C
# ch --> D
# ch --> E
# for 語句執行else子句
# 程序退出

# 練習:
#   任意輸入一個字符串，判斷這個字符串中有幾個空格' '
#   (要求不允許用S.count方法)
#   建議使用for語句實現

# s = input("請輸入一段字符串: ")

# count = 0 # 此變量用來記錄空格的個數
# for ch in s:
	#如果ch綁定空格,則將count做加1操作
	# if ch == ' ':
		# count += 1

# print("空格的個數是:", count)

# 此示例示意range函數的用法

# for x in range(4):
	# print(x)


# 0
# 1
# 2
# 3




# 練習:
  # 用for語句打印 1~20的整數，打印在一行
  # 1 2 3 4 5 6 ... 18 19 20

# for x in range(1, 21):
	# print(x, end=' ')
# else:
	# print()


# 練習:
  # 1. 求 100 以內有哪兒些整數與　自身 + 1 的乘積再對11 求餘結果等於8?

  # 2. 計算 1 + 3 + 5 + 7 +.... + 99的和
    # 用while 和 for語句兩種方法來實現

# 1.
# for x in range(100):
	# if x * (x + 1) % 11 == 8:
		# print(x)

# 2.
# s = 0

# i = 1
# while i < 100:
	# 把i累加到s變量中# 
	# s += i
	# i += 2  #因為後一前簡前一項為2


# 用for語句來實現
# for i in range(1, 100, 2):
	# s += i
# 


# print("和為", s)

# 練習:
#   1 寫程序．輸入一個整數n 代表正方形的寬度和高度．
#   打印數字組成的正方形:
#    如
#      輸入: 5
#    打印:
#     1 2 3 4 5
#     1 2 3 4 5
#     1 2 3 4 5
#     1 2 3 4 5
#     1 2 3 4 5
#    　　輸入: 4
#    打印:
#     1 2 3 4
#     1 2 3 4
#     1 2 3 4
#     1 2 3 4

# w = int(input("請輸入寬度: "))
# for _ in range(w):

	# for x in range(1, w + 1):
		# print(x, end=' ')
	# print( )



