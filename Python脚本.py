##脚本-求绝对值
am = abs(-6)
print("求绝对值: "+str(am))

##进制转化
##十进制转换为二进制
am1 = bin(10)
print("进制转换十进制转换二进制: "+str(am1))
am2 = bin(9)
print(am2)

##十进制转换为八进制
am3 =oct(9)
print("十进制转换为八进制: "+str(am3))

##十进制转换为十六进制
am4 = hex(15)
print("十进制转换为十六进制: "+str(am4))


##整数和ASCII互转
##十进制整数对应的ASCII字符
am5 = chr(65)
print("十进制整数对应ASCII: "+str(am5))

##查看某个ASCII字符对应的十进制数
am6 = ord("A")
print("查看某个ASCII对应的十进制数: "+str(am6))


##元素都为真检查
##所有元素都为真
##python中，0被视为False
am7 = all([1,0,3,6])
print("所有元素都为真检查："+str(am7))

##在python中，被视为True的情况：
##True
##任何非零数值
##任何非空对象
am8 = all([1,2,3])
print("所有元素都为真检查："+str(am8))


##至少有一个为真检查:
am9 = any([0,0,0,[]])
print("至少有一个为真检查: "+str(am9))

##至少有一个为真:
am10 = any([0,0,1])
print("至少有一个为真检查: "+str(am10))



##判断是真是假
am11 = bool([0,0,0])
print("判断是真是假: "+str(am11))

am12 = bool([])
print("判断是真是假: "+str(am12))

am14 = bool([1,0,1])
print("判断是真是假: "+str(am14))

##创建复数
am15 = complex(1,2)
print("创建一个复数: "+str(am15))

##取商和余数
am16 = divmod(10,3)
print("分别取商和余数:"+str(am16))

##转为浮点类型
am17 = float(3)


##对字符串进行批量转换为驼峰格式
import re
def camel(s):
    s = re.sub(r"(\s|_|-)+", " ", s).title().replace(" ", "")
    return s[0].lower() + s[1:]

def batch_caml(slist):
    return [camel(s) for s in slist]


s = 'this is a test str,please checkout'
sam1 = camel(s)
print("字符串转换为驼峰格式"+sam1)
sam2 = batch_caml(['student_id', 'student\tname', 'student-add'])
print(sam2)


