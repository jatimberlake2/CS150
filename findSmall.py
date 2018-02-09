items = [8, 100, 42, 0, 999, 2]
def main():
    smallest = items[0]
    for i in range(0,len(items),1):
        if (items[i] < smallest):
            smallest = items[i]
    print(smallest)
main()
