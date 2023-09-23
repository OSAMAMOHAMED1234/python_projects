col, row = map(int, input().split())
degrees = [map(float, input().split()) for _ in range(row)]
student_degrees = list(zip(*degrees))
[print(sum( student_degrees[i]) / row) for i in range(col)]