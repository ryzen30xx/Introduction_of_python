import random; s = ['apple', 'orange']; i = [1, 2, 3, 4, 5, 6, 7, 8]; f = [0.5, 1.2]; b = [True, False, False, False]; e = []; mixture = [1, '2', 3.0, True]
def list_factory():
    if 2 in i: return True
    else: return False
def call_factory():
    rd_number = random.sample(range(1, 100), 10)
    print(rd_number,"\n", len(rd_number),"\n", max(rd_number), "\n", min(rd_number), "\n", sum(rd_number), "\n", sorted(rd_number), "\n", sorted(rd_number, reverse=True))
def append_list():
    hax= i.append(f)  
    print(hax)

# # print(call_factory())
# call_factory()
#append_list()
def slice_list():
    print(i[:3])
    print(i[3:])
    print(i[::2])
    print(i[::-1])
append_list()