import random
from time import sleep
from graph_matcher import GraphMatcher

graph_matcher = GraphMatcher()


# 打字机输出效果
def print_one_by_one(line, flag=1):
    for i in range(len(line)):
        if (flag):
            print("\r" + line[0:i + 1], end="")
        else:
            print('\r' + '\033[33m' + line[0:i + 1] + '\033[0m', end="")
        sleep(0.1)


class AnswerRobot:
    def getRelations(self):
        relationList = list(random.sample(graph_matcher.getRelations(), 20))
        response = '您随机获得了如下20种关系：\n'
        for index, item in enumerate(relationList):
            response += f'{index + 1}.{item}'
            if (index + 1) % 5 == 0:
                response += '\n'
        print(response)

    def getEntities(self):
        entityList = list(random.sample(graph_matcher.getEntities(), 20))
        response = '您随机获得了如下20个实体对象：\n'
        for index, item in enumerate(entityList):
            response += f'{index + 1}.{item} '
            if (index + 1) % 5 == 0:
                response += '\n'
        print(response)

    def introduce(self):
        print_one_by_one(
            '你好，小哥哥/小姐姐，欢迎参观体验我们团队（郎文翀、黄硕、相里千卉）开发的基于哈利波特人物关系知识图谱的问答系统。\n')
        print_one_by_one('我是机器人[IKUN]，可以基于已有的400+个实体类，1.7w+关系数据回答您关于哈利波特的问题OvO！\n')
        print_one_by_one('由于开发小哥哥能力有限,我还不是那么聪明。。。。。\n')
        print_one_by_one('所以麻烦您提问时按照如下模式进行提问，否则笨笨的我暂时是看不懂问题的@……@\n')

    def help(self):
        print_one_by_one('============查询使用手册===========\n', 0)
        print_one_by_one('1. 查询某个人物的关系网请输入[关系网-哈利·波特]或者其他人物名称\n', 0)
        print_one_by_one('2. 查询两个人物的关系请输入[关系-哈利·波特-汤姆·里德尔]或者其他两个人物名称\n', 0)
        print_one_by_one('3. 查询N条具有指定关系的伙伴，请输入[伙伴-同门-20]查询显示最多20条具有同门关系的伙伴\n', 0)
        print_one_by_one(
            '4. 为了方便您进行对象查询或者关系查询，可以通过输入[对象列表]和[关系列表]查询N条信息，由于数据过多我们将随机挑选20种为您显示\n',
            0)
        print_one_by_one('5. 输入[帮助]查询使用手册\n', 0)
        print_one_by_one('6. 如果您不想咨询了请输入[辛苦IKUN了]，我就下班啦！\n', 0)

    def stop(self):
        print_one_by_one('拜拜了您嘞^_^!')
