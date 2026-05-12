class AvalancheGraph:
    def __init__(self, points_count):
        self.n = points_count
        self.states = [0] * self.n
        self.adjacency = [[0] * self.n for _ in range(self.n)]

    def connect(self, u, v):
        print(f"--- Drawing chord between Point {u} and Point {v} ---")
        
        neighbors_u = [i for i, connected in enumerate(self.adjacency[u]) if connected == 1]
        neighbors_v = [i for i, connected in enumerate(self.adjacency[v]) if connected == 1]
        
        nodes_to_flip = {u, v}
        nodes_to_flip.update(neighbors_u)
        nodes_to_flip.update(neighbors_v)
        
        for node in nodes_to_flip:
            self.states[node] = (self.states[node] + 1) % 2
            
        self.adjacency[u][v] = 1
        self.adjacency[v][u] = 1
        
        self.display_state()

    def display_state(self):
        print(f"Current States:   {self.states}")
        print("Adjacency Matrix:")
        for row in self.adjacency:
            print(f"  {row}")
        print("\n")


# ==========================================
# PROVING THE NON-ABELIAN NATURE IN CODE
# ==========================================

print("========== PATH A ==========")
print("Connecting (0 -> 1), then (1 -> 2)")
graph_a = AvalancheGraph(3)
graph_a.connect(0, 1)
graph_a.connect(1, 2)
print(f"FINAL STATE PATH A: {graph_a.states}\n")

print("========== PATH B ==========")
print("Connecting (1 -> 2), then (0 -> 1)")
graph_b = AvalancheGraph(3)
graph_b.connect(1, 2)
graph_b.connect(0, 1)
print(f"FINAL STATE PATH B: {graph_b.states}")
