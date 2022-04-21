class Graph:
    def __init__(self, edges) -> None:
        self.edges = edges
        self.graph_dict = {}

        for source, destination in self.edges:
            if source in self.graph_dict:
                self.graph_dict[source].append(destination)
            else:
                self.graph_dict[source] = [destination]

    def get_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]

        if start not in self.graph_dict.keys():
            return []

        paths = []

        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_path(node, end, path)
                for pth in new_paths:
                    paths.append(pth) 

        return paths    


    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]
        
        if start == end:
            return path

        if start not in self.graph_dict.keys():
            return None

        shortest_paths = None       
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if (shortest_paths is None) or (len(sp) < len(shortest_paths)):
                        shortest_paths = sp

        return shortest_paths

routes = [
    ("Lahore", "Paris"),
    ("Lahore", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("Dubai", "Toronto")
]

route_graph = Graph(routes)
print(route_graph.get_shortest_path("Lahore", "Toronto"))