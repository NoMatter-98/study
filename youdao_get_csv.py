
# 从：
'''
1, fluent    英译中
adj.（说话）流利的；（表达思想）熟练的，流畅的；（做事）娴熟的；畅流的，能流动的
listening
2, lounge    英译中
n.（机场等的）等候室；（旅馆、俱乐部等的）休息室；（私宅中的）起居室，客厅；<英>休闲，游荡；<美>躺椅，沙发；<英>雅座酒吧；<美>鸡尾酒酒吧
v.懒洋洋地站（或坐、躺）着；<英>百无聊赖地消磨（打发）时间
listening
'''
# 到：
'''
1, fluent
2, lounge
'''

import os
write_list = []
with open(r"C:\Users\g4560\Desktop\listening1.txt",'r',encoding='utf-8',errors='ignore') as file:
    lines = file.readlines()
    for line in lines:
        line = line.split(' ')
        if line[-1][:-1] == '英译中':
            write_list.append(line[0]+line[1]+'\n')
with open(r"C:\Users\g4560\Desktop\listening.csv",'w') as file:
    for i in range(len(write_list)):
        file.writelines(write_list[i])
