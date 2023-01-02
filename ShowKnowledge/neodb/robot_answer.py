from FinKonwledgeGraph.answer_robot import AnswerRobot
from FinKonwledgeGraph.graph_matcher import GraphMatcher

answer_robot = AnswerRobot()
graph_matcher = GraphMatcher()


def get_robot_answer(query):
    if query == '辛苦你了':
        response = answer_robot.stop()
    elif query == '帮助':
        response = answer_robot.help()
    elif query == '对象列表':
        response = answer_robot.getEntities()
    elif query == '关系列表':
        response = answer_robot.getRelations()
    elif query.split('-')[0] == '关系网' and len(query.split('-')) == 2:
        response = graph_matcher.matchGraphOfEntity(query.split('-')[1])['response']
    elif query.split('-')[0] == '关系' and len(query.split('-')) == 3:
        response = graph_matcher.matchRelationOfTwoEntities(query.split('-')[1], query.split('-')[2])
    elif query.split('-')[0] == '伙伴' and len(query.split('-')) == 3:
        response = graph_matcher.matchEntitiesByRelation(query.split('-')[1], int(query.split('-')[2]))
    else:
        response = '很抱歉，您的问题我没太理解，麻烦您再问一遍@……@'
    return response
