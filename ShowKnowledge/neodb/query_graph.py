import sys
import os

from FinKonwledgeGraph.graph_matcher import GraphMatcher


def getAvatarAndSdecription(name):
    result = {}
    avatar = "./static/images/avatars/" + name + '.jpeg'
    if os.path.exists(avatar):
        result['avatar'] = avatar
        result['description'] = "如上是「 " + name + " 」的肖像图"
    else:
        result['avatar'] = "../static/images/avatars/default.png"
        result['description'] = "暂时没有找到相关肖像，容人家再找一找"
    return result


def query(name):
    json_data = {'nodes': [], "links": [], 'html': ""}
    graph_matcher = GraphMatcher()
    rtn = graph_matcher.matchGraphOfEntity(name)
    # print(rtn)
    result = {}
    result['avatar'] = getAvatarAndSdecription(name)['avatar']
    result['description'] = getAvatarAndSdecription(name)['description']
    json_data['html'] = result_to_html(result)
    node = {
        'id': 0,
        'name': name,
        'category': 0,  # 主节点颜色不同
    }
    json_data['nodes'].append(node)
    if rtn is not None or len(rtn) != 0:
        for index, item in enumerate(rtn):
            node = {
                'id': index + 1,
                'name': item['n.名称'],
                'category': 1  # 从节点
            }
            json_data['nodes'].append(node)
            # 建立主从节点关系
            link = {
                'source': 0,  # 主节点是起始节点
                'target': index + 1,  # 从节点是目的节点
                'value': graph_matcher.formatRelation(item['r'])
            }
            json_data['links'].append(link)
        return json_data  # 返还数据
    else:
        # 结束，没有找到
        sys.exit()


def result_to_html(result):
    s = f'<img height="200px" src="{result["avatar"]}">\n <p>{result["description"]}'
    return s


# 点击echarts元素时获取信息表
def get_details(node_or_edge, data, nodes):
    result = {}
    if node_or_edge == "node":
        result['avatar'] = getAvatarAndSdecription(data['name'])['avatar']
        result['description'] = getAvatarAndSdecription(data['name'])['description']
    else:
        sys.exit()
    return result_to_html(result)
