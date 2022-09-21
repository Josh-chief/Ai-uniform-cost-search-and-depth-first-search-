graph = {
    'a': [['d', 43]],
    'b': [['g', 171]],
    'c': [['d', 126]],
    'd': [['f', 111], ['m', 200], ['o', 136]],
    'e': [['a', 133], ['l', 110]],
    'f': [['g', 88], ['h', 130]],
    'g': [['c', 140], ['d', 123], ['h', 99]],
    'h': [['n', 80]],
    'i': [['a', 109], ['c', 102]],
    'j': [['e', 105], ['i', 172], ['k', 146]],
    'k': [['e', 146], ['l', 152]],
    'l': [['o', 97]],
    'm': [['n', 67]],
    'n': [[]],
    'o': [['m', 100]]
}


def uniform_cost_search(graph, starting_node, ending_node):
    # answer: j e l o m n

    path = starting_node
    current_node = starting_node

    # check all neighbours and their costs
    # choose the neighbour with the least cost

    while current_node != ending_node:
        current_neighbours = graph[current_node]
        # example
        # graph = {'d': [['f', 111], ['m', 200], ['o', 136]]}
        # print(graph['d'])
        # [['f', 111], ['m', 200], ['o', 136]]
        minimum_cost = 10000000

        for neighbour, cost in current_neighbours:
            if cost < minimum_cost:
                minimum_cost = cost
                current_node = neighbour

        path = path + ' ' + current_node

    return path

search_path = uniform_cost_search(graph, 'j', 'n')
print('Uniform Cost Search: ' + search_path)

def depth_first_search(graph, current_node, ending_node, **kwargs):

    if current_node == ending_node:
        return current_node

    visited_nodes = kwargs.get('visited_nodes', [current_node])
    recurse_done = False
    sub_path = None

    current_neighbours = graph[current_node]

    for neighbour, cost in current_neighbours:

        if neighbour not in visited_nodes:
            recurse_done = True
            visited_nodes.append(neighbour)
            sub_path = depth_first_search(graph, neighbour, ending_node, visited_nodes=visited_nodes)

            if sub_path is not None:
                return current_node + sub_path

    if not recurse_done:
        return None


print(depth_first_search(graph, 'j', 'n'))
