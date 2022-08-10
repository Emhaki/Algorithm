list_ = []
for _ in range(3):
    list_.append(int(input()))

if list_[0] == 60 and list_[1] == 60 and list_[2] == 60:
    print("Equilateral")
elif list_[0]+list_[1]+list_[2] == 180 and (list_[0] == list_[1] or list_[1] == list_[2] or list_[2] == list_[0]):
    print("Isosceles")
elif list_[0]+list_[1]+list_[2] == 180 and (list_[0] != list_[1] != list_[2]):
    print("Scalene")
elif list_[0]+list_[1]+list_[2] != 180:
    print("Error")