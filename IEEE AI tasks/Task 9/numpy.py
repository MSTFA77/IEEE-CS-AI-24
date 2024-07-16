import random

def alternating_maximum_sum(array):
  """
  Calculates the maximum sum achievable by two players who take turns picking
  elements from opposite ends of a sorted array, maximizing their own score.

  Args:
      array: A list of integers representing the elements to be picked.

  Returns:
      A tuple containing the maximum scores for players 1 and 2.
  """

  n = len(array)
  array.sort()  # Sort the array in ascending order

  player1_score = 0
  player2_score = 0
  turn = 0  # Keep track of whose turn it is

  for i in range(n):
    if turn % 2 == 0:
      player1_score += array[i]
    else:
      player2_score += array[i]
    turn += 1

  return player1_score, player2_score

# Example usage
n = int(input("Enter the size of the array: "))
array = [random.randint(1, 100) for _ in range(n)]  # Randomly generate array elements
print("Input array:", array)

player1_score, player2_score = alternating_maximum_sum(array.copy())  # Copy to avoid modifying original array
print("Maximum score for Player 1:", player1_score)
print("Maximum score for Player 2:", player2_score)
