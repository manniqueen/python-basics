import math
length = float(input())
width = float(input())
wardrobeSide = float(input())
hallArea = (length* 100) * (width * 100)
wardrobeArea = (wardrobeSide * 100) * (wardrobeSide * 100)
benchArea = hallArea / 10
freeSpace = hallArea - wardrobeArea-benchArea
dancers = math.floor(freeSpace / 7040)
print('%.0f' % dancers)

