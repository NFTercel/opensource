#coding=utf-8
import itertools;
import random
import string
# a=[1,2,3];
# b=[4,5,6];
# a = '不行;广大;大幅度;老;充分;大钱;大规模;特大;爸爸;俊雅;可怜;死;杀'.split(';')
# b = '常温;超低温;高温;恒温;候温;炉温;气温;室温;水温;体温'.split(';')
# print("a,b的笛卡尔乘积：")
# for x in itertools.product(a,b):
#     print(x[0], x[1])
# print()
# print("a自身的笛卡尔乘积：")
# for x in itertools.product(a,a):
#     print(x[0], x[1])

# import time
#
# def get_time(type=None):
#     if type == None:
#         nowtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#     else:
#         nowtime = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
#     print('Time: ',nowtime)
#     return nowtime


def get_random_str(type,num,count=None):
    data = ''
    strarr = []
    if count == None:
        count = 1

    if type == "d":
        data = string.digits
    elif type == "low":
        data = string.ascii_lowercase
    elif type == "upper":
        data = string.ascii_uppercase
    elif type == "l":
        data == string.ascii_letters
    elif type == "dl":
        data = string.digits + string.ascii_letters
    elif type == "dlp":
        data = string.digits + string.ascii_letters + string.punctuation
    print('data: ',data)
    print('count: ',count)
    print('num: ',num)
    for i in range(count):
        str = random.sample(data, num)
        strarr.append(''.join(str))
    print("string list: ",strarr)
    return strarr

get_random_str('dl',10,12)