import heapq
from collections import defaultdict

class UserData:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, purchases):
        self.users[user_id] = purchases

    def get_purchases(self, user_id):
        return self.users.get(user_id, [])


class ProductGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, product, related_product):
        self.graph[product].append(related_product)

    def get_related(self, product):
        return self.graph.get(product, [])


class RecommendationEngine:
    def __init__(self, user_data, product_graph):
        self.user_data = user_data
        self.product_graph = product_graph

    def recommend(self, user_id):
        purchases = self.user_data.get_purchases(user_id)
        scores = defaultdict(int)

        for item in purchases:
            for related in self.product_graph.get_related(item):
                if related not in purchases:
                    scores[related] += 1

        heap = []
        for product, score in scores.items():
            heapq.heappush(heap, (-score, product))

        recommendations = []
        while heap and len(recommendations) < 5:
            score, product = heapq.heappop(heap)
            recommendations.append((product, -score))

        return recommendations


if __name__ == "__main__":
    user_data = UserData()
    graph = ProductGraph()

    user_data.add_user("user1", ["Laptop", "Phone"])
    user_data.add_user("user2", ["Laptop"])
    user_data.add_user("user3", ["Phone", "Tablet"])

    graph.add_edge("Laptop", "Mouse")
    graph.add_edge("Laptop", "Keyboard")
    graph.add_edge("Phone", "Earbuds")
    graph.add_edge("Phone", "Charger")
    graph.add_edge("Tablet", "Case")
    graph.add_edge("Tablet", "Stylus")

    engine = RecommendationEngine(user_data, graph)

    print("Recommendations for user1:")
    print(engine.recommend("user1"))

    print("\nRecommendations for user2:")
    print(engine.recommend("user2"))

    print("\nRecommendations for user3:")
    print(engine.recommend("user3"))