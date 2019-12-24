# random.random()函数是这个模块中最常用的方法了，它会生成一个随机的浮点数，范围是在0.0~1.0之间。
# random.uniform()正好弥补了上面函数的不足，它可以设定浮点数的范围，一个是上限，一个是下限。
# random.randint()随机生一个整数int类型，可以指定这个整数的范围，同样有上限和下限值，python random.randint。
# random.choice()可以从任何序列，比如list列表中，选取一个随机的元素返回，可以用于字符串、列表、元组等。
# random.shuffle()如果你想将一个序列中的元素，随机打乱的话可以用这个函数方法。
# random.sample()可以从指定的序列中，随机的截取指定长度的片断，不作原地修改

# String模块中的常量：
# string.digits：数字0~9
# string.letters：所有字母（大小写）
# string.lowercase：所有小写字母
# string.printable：可打印字符的字符串
# string.punctuation：所有标点
# string.uppercase：所有大写字母

#请填写用户名，格式为2-20个字符，可以为字母，数字和中文”
# import random,string
# src_digits = string.digits  # string_数字
# src_letters=string.ascii_letters    #所有字母
# # 随机生成数字、大小写字母的组成个数（可根据实际需要进行更改）
# digits_num = random.randint(1, 10)
# print(digits_num)
# letters_num = random.randint(1, 20 - digits_num-1)
# print(letters_num)
# # 生成字符串
# username1 = random.sample(src_digits, digits_num) + random.sample(src_letters,letters_num)
# #拼接中文
# chinese_num=random.randint(1,20-digits_num-letters_num)
# print(chinese_num)
# for i in range(1,chinese_num+1):
#     # 生成随机中文
#     head = random.randint(0xb0, 0xf7)
#     body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
#     val = f'{head:x}{body:x}'
#     src_chinese = bytes.fromhex(val).decode('gb2312')
#     username1+=src_chinese
# print(username1)
# # 打乱字符串
# random.shuffle(username1)
# print(username1)
# # 列表转字符串
# username= ''.join(username1)
# print(username)

# for i in range(1,100):
#     val = random.randint(0x4e00, 0x9fbf)
#     print(chr(val))

# a = 1
# b = 1
# print(id(a))
# print(id(b))
# print(id(a) == id(b))

# str = 'aabbccdeff'
# a = []
# for i in str:
#     if i not in a:
#         a .append(i)
# print(a)

# numbers = [1,2,3,4]
# numbers = [ str(x) for x in numbers ]
# print(numbers)
import random
# print(random.randint(0,0))
random_digits = []
for i in range(0, random.randint(0, 16)):
    print(i)
    random_digits.append(random.randint(0, 9))
random_digits = [str(x) for x in random_digits]
print(random_digits)
