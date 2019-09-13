import numpy as np
from tqdm import tqdm
np.set_printoptions(threshold=np.inf)


class Graph:

    def __init__(self):

        self.num_vertices = 0
        self.num_edges = 0
        self.num_edges_test = 0

        self.adjacency_matrix = None

    def parse_txt(self, path):
        print("Parsing txt to graph representation ...")
        with open(path, 'r') as f:
            lines = f.readlines()
            self.num_vertices = len(lines)
            self.adjacency_matrix = np.zeros([self.num_vertices, self.num_vertices], dtype=np.int32)
            print("Number of vertices", self.num_vertices)
            for vertex_id, line in enumerate(lines):
                adjacent_vertices = [int(elem)-1 for elem in line.split()]
                for adjacent_vertex in adjacent_vertices[1:]:
                    self.adjacency_matrix[vertex_id, adjacent_vertex] += 1
            self.num_edges = np.sum(self.adjacency_matrix)/2
            print("Number of edges", self.num_edges)

    def test_integrity(self):
        #print("Trace of adjacency_matrix", np.trace(self.adjacency_matrix))
        assert(np.trace(self.adjacency_matrix) == 0)
        assert(np.all(self.adjacency_matrix < 2))
        assert(np.array_equal(self.adjacency_matrix, self.adjacency_matrix.T))

    def generate_test_graph(self):
        self.adjacency_matrix = np.array([
            [0, 1 ,0, 0, 0],
            [1, 0 ,1, 1, 1],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0],
            ], dtype=np.int32)

    def karger_min_cut(self, iterations=10):
        min_cut = self.karger_min_cut_once()
        for i in tqdm(range(iterations-1)):
            min_cut = min(self.karger_min_cut_once(), min_cut)
            print("Current min cut", min_cut)
        return min_cut

    def karger_min_cut_once(self):
        graph = np.copy(self.adjacency_matrix)

        while(graph.shape[0] > 2):
            graph = self.merge_random_vertex_pair(graph)

        return graph[0, 1]


    def merge_random_vertex_pair(self, graph):
        edge = self.choose_random_edge(graph)

        # Move edges of second vertex to first one
        graph[edge[0], :] += graph[edge[1], :]
        graph[:, edge[0]] += graph[:, edge[1]]
        
        # Remove self loops
        np.fill_diagonal(graph, 0)

        # Delete processed second vertex
        graph = np.delete(graph, edge[1], 0)
        graph = np.delete(graph, edge[1], 1)
        return graph

    def choose_random_edge(self, graph):
        edges = np.argwhere(graph > 0)
        random_indice = np.random.randint(len(edges)-1)
        return edges[random_indice]


if __name__=="__main__":
    graph = Graph()
    graph.parse_txt("./kargerMinCut.txt")
    graph.test_integrity()
    print("Calculating min cut")
    print(graph.karger_min_cut(200000))