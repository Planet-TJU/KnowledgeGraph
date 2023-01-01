from py2neo import Graph


class GraphMatcher:
    '''
    创建基于Cypher语句的neo4j数据库查询方法封装对象
    '''

    def formatRelation(self, relation):
        return str(relation).split(':')[1].split(' ')[0]

    def __init__(self):
        self.graph = Graph('bolt://localhost:7687', auth=('neo4j', 'neo4j123'))

    def matchGraphOfEntity(self, entity):
        '''
        :param entity:
        :return: String
        实现根据某个实体查询返回所有和他相关的节点关系
        '''
        cypher_sql = f'match (m)-[r]->(n) where m.名称 = "{entity}" return r,n.名称'
        rtn = self.graph.run(cypher_sql).data()
        if rtn is not None or len(rtn) != 0:
            response = f'{entity}的相关信息如下：\n'
            for index, item in enumerate(rtn):
                relation = self.formatRelation(item['r'])
                obj = item['n.名称']
                response += f'{index + 1}、 {entity}的{relation}是{obj}\n'
            # print(response)
        return rtn

    def matchRelationOfTwoEntities(self, entity1, entity2):
        '''
        # 获取两个实体之间的关系
        :param entity1:
        :param entity2:
        :return:
        '''
        cypher_sql = f'match (m)-[r]->(n) where m.名称="{entity1}" and  n.名称="{entity2}" return r'
        rtn = self.graph.run(cypher_sql).data()
        if rtn is not None and len(rtn) != 0:
            relation = self.formatRelation(rtn[0]['r'])
            response = f'{entity1}的{relation}是{entity2}\n'
        else:
            response = f'您查询的两个人物实体暂时没有任何关系！'
        print(response)

    def matchEntitiesByRelation(self, relation, nums):
        '''
        # 获取最多nums条相关关系的节点集合
        :param relation:
        :param nums:
        :return:
        '''
        cypher_sql = f'match (m)-[r:{relation}]->(n)  return m.名称,n.名称 limit {nums}'
        rtn = self.graph.run(cypher_sql).data()
        if rtn is not None or len(rtn) != 0:
            response = f'具有{relation}关系的实体集合如下：\n'
            for index, item in enumerate(rtn):
                # print(item)
                entity1 = item['m.名称']
                entity2 = item['n.名称']
                response += f'{index + 1}、 {entity1}的{relation}是{entity2}\n'
            print(response)

    def getEntities(self):
        # 获取所有实体
        cypher_sql = f'match (n) return n.名称'
        rtn = self.graph.run(cypher_sql).data()
        entityList = []
        for item in rtn:
            entityList.append(item['n.名称'])
        return entityList

    def getRelations(self):
        #         获取所欲关系
        cypher_sql = f'MATCH r=()-->() RETURN r limit 2000'
        rtn = self.graph.run(cypher_sql).data()
        relationSet = set()
        for index, item in enumerate(rtn):
            # print(item)
            relationSet.add(self.formatRelation(item['r']))
        return relationSet
