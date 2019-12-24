import random,string

class Random_Number():

    def random_username(self):
        #用户名必须由3-15个字符或者2-7个汉字组成
        min_number=3
        max_number=15
        #生成0-15个随机数字
        random_digits=[]
        for i in range(0,random.randint(0,15)):
            random_digits.append(random.randint(0,9))
        random_digits = [str(x) for x in random_digits]
        # 生成0-15个随机字母（与数字个数总数小于等于15）
        src_letters=string.ascii_letters    #所有字母
        letters_num = random.randint(0, max_number - len(random_digits))
        # 生成数列：数字+字母
        username1 =  random_digits+random.sample(src_letters,letters_num)
        dig_let_count=len(username1)
        #拼接中文
        if dig_let_count<min_number:
            zhongwen1=min_number - dig_let_count
            if zhongwen1%2==0:
                min_chinese=zhongwen1/2
                max_chinese=(max_number-zhongwen1)/2
                print(min_chinese,max_chinese)
                chinese_num=random.randint(min_chinese,max_chinese)
            else:
                min_chinese = (min_number - dig_let_count) + 1
                max_chinese = (max_number-zhongwen1)//2+1
                chinese_num = random.randint(min_chinese, max_chinese)
        elif min_number<=dig_let_count<=max_number:
            zhongwen2 = max_number - dig_let_count
            if zhongwen2 % 2 == 0:
                min_chinese = 0
                max_chinese = zhongwen2 / 2
                chinese_num = random.randint(min_chinese, max_chinese)
            else:
                min_chinese = 0
                max_chinese = zhongwen2 // 2
                chinese_num = random.randint(min_chinese, max_chinese)
        for i in range(0,chinese_num):
            # 生成随机中文
            head = random.randint(0xb0, 0xf7)
            body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
            val = f'{head:x}{body:x}'
            src_chinese = bytes.fromhex(val).decode('gb2312')
            username1.append(src_chinese)
        # 打乱字符串
        random.shuffle(username1)
        # 列表转字符串
        username= ''.join(username1)
        return username

