class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        distance = list[list]
        distance[x][y] = 1
        distance[y][x] = 1
        

    def graph(self, n: int, x: int, y: int) -> list[list[int]]:
        i = 1
        graph = [[]]
        graph[0] = [0] * n
        while i <= n:
            j = 1
            temp = []
            temp.append(0)
            while j <= n:
                if (x == i and y == j) or (x == j and y == i):
                    temp.append(1)
                    j += 1
                    continue

                temp.append(abs(i-j))
                j += 1

            graph.append(temp)
            i += 1

        return graph
    
    def FloydWarshall(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph)
        distance = graph.copy()
        

        return distance
            

def main():
    Sol = Solution()
    graph = Sol.graph(4, 1, 3)
    print(Sol.FloydWarshall(graph))


if __name__ == "__main__":
    main()