from tqdm import tqdm
import pandas as pd
from py2neo import Graph, Node, Relationship, NodeMatcher

'''
连接Neo4j
'''

graph = Graph('bolt://localhost:7687', auth=('neo4j', '123456'))
# 创建搜索器
matcher = NodeMatcher(graph)
print(graph)
graph.run('match (n) detach delete n')  # 删除所有节点及其关系

'''
创建哈利波特实体
'''
print('创建哈利波特实体')
harrypotter_net = pd.read_csv('./data/harrypotterkgdata.csv')
entitySet = set()
for idx, each_row in tqdm(harrypotter_net.iterrows()):
    # 实体去重
    entitySet.add(each_row['entity1'])
    entitySet.add(each_row['entity2'])
#     创建实体
for item in entitySet:
    # print(item)
    each_entity = Node('实体',
                       名称=item)
    try:
        graph.create(each_entity)
    except Exception as e:
        print(f'Error on : {e},data:{item}')

'''
创建哈利波特关系网
'''
for idx, each_row in tqdm(harrypotter_net.iterrows()):
    node1 = matcher.match('实体', 名称=each_row['entity1']).first()
    node2 = matcher.match('实体', 名称=each_row['entity2']).first()
    if node1 is not None and node2 is not None:
        r = Relationship(node1, each_row['relation'], node2)
        graph.create(r)

print('已创建完成')
