if dist[x][y][0] > dist[x][k][0]+dist[k][y][0]:
        dist[x][y][0] = dist[x][k][0]+dist[k][y][0]
        dist[x][y][1] = dist[x][k][1]+dist[k][y][1]+A[k]
      elif dist[x][y][0] == dist[x][k][0]+dist[k][y][0]:
        dist[x][y][1] = min(dist[x][y][1], dist[x][k][1]+dist[k][y][1]+A[k])