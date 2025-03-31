n, m = map(int, input().split())

anya_colors = {int(input()) for _ in range(n)}
borya_colors = {int(input()) for _ in range(m)}

common_colors = sorted(anya_colors & borya_colors)
only_anya_colors = sorted(anya_colors - borya_colors)
only_borya_colors = sorted(borya_colors - anya_colors)

print(len(common_colors))
print(*common_colors)
print(len(only_anya_colors))
print(*only_anya_colors)
print(len(only_borya_colors))
print(*only_borya_colors)
