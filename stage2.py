wind_zones = [((4, 3), 1.5), ((7, 2), 1.2)]

# Check and reroute (simple detour demo)
def is_in_wind_zone(p1, p2, zones):
    for center, radius in zones:
        cx, cy = center
        # Approximate mid-point
        mx, my = (p1[0]+p2[0])/2, (p1[1]+p2[1])/2
        if np.hypot(mx-cx, my-cy) < radius:
            return True
    return False

adjusted_path = [path[0]]
for i in range(1, len(path)):
    a, b = waypoints[path[i-1]], waypoints[path[i]]
    if is_in_wind_zone(a, b, wind_zones):
        # Detour: add offset point
        offset = [a[0]+0.5, a[1]+1.5]
        waypoints = np.vstack([waypoints, offset])
        adjusted_path.append(len(waypoints)-1)
    adjusted_path.append(path[i])

# Plot adjusted route
plt.figure(figsize=(8,6))
for i in range(len(adjusted_path)-1):
    a, b = waypoints[adjusted_path[i]], waypoints[adjusted_path[i+1]]
    plt.plot([a[0], b[0]], [a[1], b[1]], 'go-')

# Plot wind zones
for center, r in wind_zones:
    circle = plt.Circle(center, r, color='skyblue', alpha=0.4)
    plt.gca().add_patch(circle)

plt.scatter(waypoints[:,0], waypoints[:,1], c='red')
plt.title("Stage 2: Adjusted Route (Avoiding Wind Zones)")
plt.grid(True)
plt.show()