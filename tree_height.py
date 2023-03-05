# python3 Darja Sevcova 221RDC039 

import sys
import threading
import numpy


def compute_height(n, parents):
    ch = [[] for _ in range(n)]
    tree = None

    for a, b in enumerate(parents):
        if b == -1:
            tree = a
        else:
            ch[b].append(a)

    def max_heigth(value):
        heigth = 1

        if not ch[value]:
            return heigth
        else:
            for child in ch[value]:
                heigth = max(heigth, max_heigth(child))

            return heigth + 1    
    return max_heigth(tree)

def main():
    text = input("Enter data from the console:")
    if "I" in text:
        n = int(input("Enter the number of nodes:"))
        parents = list(map(int, input().split()))
    elif "F" in text:
        fileName = input("Enter the file name:")
        path = './test/'
        filePath = os.path.join(path, fileName)
        if "a" in fileName:
            print("Error: Invalid file name")
            return

        else:
            try:
                with open (filePath) as file:
                    p = int(file.readLine())
                    parents = list(map(int, file.readLine().split()))
            except Exception as error:
                print("Error:", str(error))
                return

    else:
        print("Error: Enter 'I' for console input or 'F' for file input")
        return

    print("The heigth of the tree is:", compute_height(n, parents))
    
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
