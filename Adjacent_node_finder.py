import numpy as np

given_matrix = np.array([
    0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0
], np.int16)
matrix = given_matrix.reshape(5, 5)
matrix_bool = matrix == 1


def adjacent_node(element, row):
  try:
    print(matrix_bool[element, row])
  except IndexError:
    print("Node out of range")


node1 = int(input("Provide first node (0-4): "))
node2 = int(input("Provide second node (0-4): "))
adjacent_node(node1, node2)
