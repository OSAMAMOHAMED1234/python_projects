from math import atan2, degrees, pi
ab = float(input())
bc = float(input())
print(f'{str(round(degrees(atan2(ab, bc))))}{chr(176)}')
# print(f'{str(round(degrees(atan2(ab, bc))))}°')
# print(str(round(atan2(ab, bc) * 180 / pi)) + '°')