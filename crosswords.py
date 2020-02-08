from random import shuffle, randint
from copy import deepcopy
ans = [
    '汤圆',
    '火锅',
    '串串香',
    '椒麻鸡',
    '烟熏三文鱼',
    '牛蛙',
    '豆汤',
    '豌豆苗',
    '焗蟹煲',
    '凉皮',
    '烤鸭',
    '菠菜芝士意大利馄饨',
    '清蒸黄鱼',
    '手剥笋',
    '酸汤肥牛',
    '糯米糍粑',
    '酸汤鱼',
    '冰粉',
    '麻辣兔头',
    '小酥肉',
    '杏仁豆腐',
    '鲜芋仙',
    '芥末鸡条',
    '肉夹馍',
    '奶油蘑菇汤',
    '披萨',
    '皮蛋豆腐',
    '番茄猪软骨面',
    '糖渍小番茄',
    '葱油拌面',
    '炸薯条',
    '南部酥脆鸡翅',
    '芝士条',
    '洋葱圈',
    '巧克力芭菲',
    '肉松面包',
    '冒鸭血',
    '果仁菠菜',
    '烤鸡肉卷',
    '酸菜白肉',
    '西班牙海鲜饭',
    '炸响铃萝卜',
    '咸蛋黄波波',
    '冰米酒酿奶',
    '百香果双响炮',
    '奶茶三兄弟',
    '芋头泥石流',
    '青稞奶茶',
    '泡鲁达',
    '豚骨拉面',
    '炸香蕉',
    '卤大肠',
    '蓝莓芝士派',
    '丝娃娃',
    '东坡肉',
    '糖醋小排',
    '咖喱蛋包饭',
    '剁椒鱼头',
    '小炒牛肉',
    '小龙虾',
    '无花果',
    '黄米凉糕',
    '双皮奶',
    '杨枝甘露',
    '手抓饼',
    '螺蛳粉'
    ]
chars = ''.join(ans)
ROW = 10
COLUMN = 10
single_line = ['字'] * COLUMN 
board = []
for i in range(ROW):
    board.append(deepcopy(single_line))

def print_board(board):
    for r in board:
        for c in r:
            print(c,end='')
        print('')

# print_board(board)
shuffle(ans)
count = 0
for i in range(20):
    item = ans[i]
    direct = randint(0,9) #0-3=horizonal,4-7=vertical,8=p-dia,9=d-dia
    ninterrupt = True
    if direct <= 3:
        x = randint(0,ROW-1)
        y = randint(0,COLUMN-len(item))
        for r in range(len(item)):
            if board[x][y+r] != '字':
                ninterrupt = False
                break
        if ninterrupt:
            for r in range(len(item)):
                board[x][y+r] = item[r]
    elif direct <= 7:
        x = randint(0,ROW-len(item))
        y = randint(0,COLUMN-1)
        for r in range(len(item)):
            if board[x+r][y] != '字':
                ninterrupt = False
                break
        if ninterrupt:
            for r in range(len(item)):
                board[x+r][y] = item[r]
    elif direct == 8:
        x = randint(0,ROW-len(item))
        y = randint(0,COLUMN-len(item))
        for r in range(len(item)):
            if board[x+r][y+r] != '字':
                ninterrupt = False
                break
        if ninterrupt:
            for r in range(len(item)):
                board[x+r][y+r] = item[r]
    elif direct == 9:
        x = randint(0,ROW-len(item))
        y = randint(len(item)-1,COLUMN-1)
        for r in range(len(item)):
            if board[x+r][y-r] != '字':
                ninterrupt = False
                break
        if ninterrupt:
            for r in range(len(item)):
                board[x+r][y-r] = item[r]
    if ninterrupt:
        count += 1
# print('==================')   
# print_board(board)
for i in range(ROW):
    for j in range(COLUMN):
        if board[i][j] == '字':
            board[i][j] = chars[randint(0, len(chars)-1)]
# print('==================')    
print('本题共有至少',count,'个答案\n========================')
print_board(board)
