from random import randint

def gen_random(count, min, max):
    rand_int_list = []
    for i in range(count):
        rand_int_list.append(randint(min, max))
    return rand_int_list

def main():
    print('gen_random.py')
    print(*gen_random(5, 1, 3), sep=', ')

if __name__ == "__main__":
    main()
