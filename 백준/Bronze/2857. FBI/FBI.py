list_ = []
for i in range(5):
    FBI = input()
    if FBI.find('FBI') != -1:
        list_.append(str(i+1))

if len(list_) == 0:
    print("HE GOT AWAY!")
else:
    print(" ".join(list_))