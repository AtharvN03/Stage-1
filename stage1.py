     import numpy as np
             import matplotlib.pyplot as plt
            from scipy.spatial.distance import cdist
            from itertools import permutations

            # Sample waypoint coordinates (x, y)
            waypoints = np.array([
            [0, 0], [2, 3], [5, 2], [6, 6], [8, 3], [10, 0]])

            # Calculate distance matrix
            dist_matrix = cdist(waypoints, waypoints)

           # Brute-force TSP (for demonstration, not scalable)
           def tsp_brute_force(matrix):
            n = len(matrix)
            best_path = None
            min_cost = float('inf')
            for perm in permutations(range(1, n)):
            path = [0] + list(perm) + [0]
            cost = sum(matrix[path[i], path[i+1]] for i in range(n))
            if cost < min_cost:
            min_cost = cost
            best_path = path
            return best_path, min_cost

            path, cost = tsp_brute_force(dist_matrix)

            print("Optimized Path:", path)
            print("Total Distance:", cost)

            # Plot
            plt.figure(figsize=(8,6))
            for i in range(len(path)-1):
              a, b = waypoints[path[i]], waypoints[path[i+1]]
            plt.plot([a[0], b[0]], [a[1], b[1]], 'bo-')
            plt.scatter(waypoints[:,0], waypoints[:,1], c='red')
            plt.title("Stage 1: Initial Optimized Route")
            plt.grid(True)
            plt.show()  