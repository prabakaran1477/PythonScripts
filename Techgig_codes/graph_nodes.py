graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']
         }


'''
def find_path(graph, start, end, path=[]):
    print(' =:= ',graph[start])
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None
print(graph)
# val = find_path(graph, 'A', 'D')
# print(val)
'''

def minRoads(input1):
    graph,start,end = input_to_graph(input1)
    print ('graph : ', graph)
    def path_finder(graph,start,end,path =[]):
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        for n in graph[start]:
            print(' = ',n)
            if n not in path:
                newpath = path_finder(graph, n, end, path)
                print(newpath)
                input('***')
                if newpath: return newpath
        return None

    # output = path_finder(graph, start, end)
    # return output
    def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        print(shortest)
        return shortest

    # value = find_shortest_path(graph, start, end)
    # print(value)
    # input()

    def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
    value = find_all_paths(graph, start, end)
    print(value)
    print(len(value))
    input()


    def to_close_path(graph,start,end,input1):
        out = []
        for node in graph:
            if end in graph[node]:
                # print('end  :  ',end)
                # print('node  :  ',node)
                for check in input1:
                    print ('check  :  ',check)
                    if (str(end) in check and str(node) in check):

                        out.append(node)

        return len(node)

    # val = to_close_path(graph, start, end,input1)
    # g = nx.Graph(graph)
    # print(val)
    # return val
import itertools
def input_to_graph(list1):
    graph = {}
    value = [i.split('#') for i in list1]
    for i in value:
        if i[0] not in graph:
            graph[i[0]] = []
            graph[i[0]].append(i[1])
        else:
            graph[i[0]].append(i[1])
    start = list1[0].split('#')[0]
    end = list1[-1].split('#')[1]
    print('start : ',start)
    print('end : ',end)
    print ('graph = = ', graph)
    return graph,start,end



final_op = minRoads(['1#2', '1#5', '2#5', '2#3','6#3', '3#4', '4#5', '4#6'])
print(final_op)


{
    '1': ['2', '5'],
    '2': ['5', '3'],
    '6': ['3'],
    '3': ['4'],
    '4': ['5', '6']
}
