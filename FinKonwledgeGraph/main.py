from graph_matcher import GraphMatcher
from answer_robot import AnswerRobot

graph_matcher = GraphMatcher()

answer_robot = AnswerRobot()
# answer_robot.introduce()
# answer_robot.help()
while True:
    query = input('用户：')
    if query == '辛苦IKUN了':
        answer_robot.stop()
        break
    elif query == '帮助':
        answer_robot.help()
    elif query == '对象列表':
        answer_robot.getEntities()
    elif query == '关系列表':
        answer_robot.getRelations()
    elif query.split('-')[0] == '关系网' and len(query.split('-')) == 2:
        graph_matcher.matchGraphOfEntity(query.split('-')[1])
    elif query.split('-')[0] == '关系' and len(query.split('-')) == 3:
        graph_matcher.matchRelationOfTwoEntities(query.split('-')[1], query.split('-')[2])
    elif query.split('-')[0] == '伙伴' and len(query.split('-')) == 3:
        graph_matcher.matchEntitiesByRelation(query.split('-')[1], int(query.split('-')[2]))
    else:
        print('很抱歉，您的问题我没太理解，麻烦您再问一遍@……@')
