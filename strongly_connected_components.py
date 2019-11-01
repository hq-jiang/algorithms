#!/usr/bin/python3

import sys
sys.setrecursionlimit(200000)


class Graph(object):
    
    def __init__(self):

        self.adjacency_list = []
        self.num_edges = 0
        self.num_vertices = 0
        self.num_explored_vertices = 0

    def read_txt(self, path):

        with open(path, 'r') as file:
            print('Parsing graph ...')
            lines = file.readlines()

            self.num_vertices = 875714
            self.adjacency_list = [[] for i in range(self.num_vertices)]
            for line in lines:
                edge = line.strip('\n').split()
                from_vertex = int(edge[0]) - 1
                to_vertex = int(edge[1]) - 1
                self.adjacency_list[from_vertex].append(to_vertex)
        self.num_edges = self.count_num_edges()

        assert len(lines) == self.num_edges, "Number of edges not consistent"
        print('Number of edges', self.num_edges)
        print('Number of vertices', self.num_vertices)

        print('Head of the adjacency list:')
        self.print(self.adjacency_list[:10])

    def print(self, adjacency_list):
        for i, vertices in enumerate(adjacency_list):
            print("Vertex id:", i, "->", vertices)

    def count_num_edges(self):
        num_edges = 0
        for vertex in self.adjacency_list:
            num_edges += len(vertex)
        return num_edges

    def create_test_graph(self):
        self.reset()

        print('Creating test graph ...')
        self.adjacency_list = [
            [2, 3],     # 0
            [0],        # 1
            [1],        # 2
            [2, 4],     # 3
            [5, 7],     # 4
            [6],        # 5
            [4],        # 6
            [],         # 7
            [6]         # 8
        ]
        
        self.num_vertices = len(self.adjacency_list)

        self.num_edges = self.count_num_edges()

        print('Number of edges:', self.num_edges)
        print('Number of vertices:', self.num_vertices)
        print('Adjacency list of test graph:')
        self.print(self.adjacency_list)

    def reset(self):
        pass

    def strongly_connected_components(self):
        reverse_adjacency_list = self.reverse(self.adjacency_list)
        print("First Pass ...")
        finishing_times = self.first_pass_depth_first_search(reverse_adjacency_list)
        print(finishing_times)
        magic_order = [0] * len(finishing_times)
        for vertex, time in enumerate(finishing_times):
            magic_order[time] = vertex
        magic_order.reverse()
        print(magic_order)
        print("Second Pass ...")
        scc = self.second_pass_depth_first_search(self.adjacency_list, magic_order)
        print("Strongly connected components", scc)
        return scc

    def first_pass_depth_first_search(self, adjacency_list, verbose=True):
        explored = [False] * self.num_vertices
        finishing_times = [0] * self.num_vertices
        recursion_depth = 0
        loop_count = 0
        lowest_unexplored_vertex = 0
        self.num_explored_vertices = 0

        while lowest_unexplored_vertex < self.num_vertices:
            loop_count += 1
            print("Loop", loop_count)
            for vertex in range(lowest_unexplored_vertex, self.num_vertices):
                lowest_unexplored_vertex = vertex + 1
                if not explored[vertex]:
                    self._depth_first_search(adjacency_list,
                                             vertex,
                                             explored,
                                             recursion_depth,
                                             finishing_times=finishing_times)
                    break
        assert all(explored), "Not all vertices have been explored"
        if verbose:
            print(explored)
        return finishing_times

    def second_pass_depth_first_search(self, adjacency_list, magic_order, verbose=True):
        explored = [False] * self.num_vertices
        finishing_times = [0] * self.num_vertices
        recursion_depth = 0
        loop_count = 0
        lowest_unexplored_vertex = 0
        self.num_explored_vertices = 0
        strongly_connected_components = []

        while lowest_unexplored_vertex < self.num_vertices:
            component = []
            loop_count += 1
            print("Loop", loop_count)

            for next_in_order in range(lowest_unexplored_vertex, self.num_vertices):
                lowest_unexplored_vertex = next_in_order + 1
                if not explored[magic_order[next_in_order]]:
                    self._depth_first_search(adjacency_list,
                                             magic_order[next_in_order],
                                             explored,
                                             recursion_depth,
                                             component=component)
                    break

            if component:
                strongly_connected_components.append(component)
        assert all(explored), "Not all vertices have been explored"
        if verbose:
            print(explored)
        return strongly_connected_components

    def _depth_first_search(self,
                            adjacency_list,
                            vertex,
                            explored,
                            recursion_depth,
                            finishing_times=None,
                            component=None,
                            verbose=False):
        recursion_depth += 1
        if component is not None:
            component.append(vertex)

        print("recursion depth", recursion_depth, "\t Vertices explored", self.num_explored_vertices)
        explored[vertex] = True
        if verbose:
            print(vertex)
        for next_vertex in adjacency_list[vertex]:
            if not explored[next_vertex]:
                self._depth_first_search(adjacency_list,
                                         next_vertex,
                                         explored,
                                         recursion_depth,
                                         finishing_times=finishing_times,
                                         component=component)
        if finishing_times is not None:
            finishing_times[vertex] = self.num_explored_vertices
        self.num_explored_vertices += 1

    def reverse(self, adjacency_list):
        reverse_adjacency_list = [[] for i in range(self.num_vertices)]
        for i, vertices in enumerate(adjacency_list):
            for vertex in vertices:
                reverse_adjacency_list[vertex].append(i)

        print('Head of adjacency list of reversed graph:')
        self.print(reverse_adjacency_list[:10])
        return reverse_adjacency_list


if __name__=='__main__':
    graph = Graph()
    graph.read_txt('./SCC.txt')
    # graph.create_test_graph()
    scc = graph.strongly_connected_components()
    scc_sizes = [len(component) for component in scc]
    scc_sizes.sort(reverse=True)
    print(scc_sizes[:1000])
    print("Done")