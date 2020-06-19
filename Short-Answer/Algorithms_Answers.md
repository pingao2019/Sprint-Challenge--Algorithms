#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  a = 0
    while (a < n * n * n):
      a = a + n * n

 Answer:  O(n),   # a is increased by n**2(a constant) each loop,  its constanstly grows depending on input size
 

b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1

Answer: O(n (logn+n)).
The  outer layer is run time with n, inner layer integer squared with each iteration  and sum up, run time with log n +n.  


   

c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

Answer: O(n).
 The time increase when the number of inputs increases.
  

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.


Answer: 

The total floors number is  n. f is the floor we are looking for. if the floors  >= f, egg broken; if the floor < f, egg not broken. To find this floor.

My plan would use binary  searching algorithms to save searching space time. I will set floor == n/2 as the base . and check if the egg breaks from there. If I find  this floor where the egg == broken, this floor is still high. So repeatedly,  I will  search left branch until I find the floor which egg can not broken.  Binary  searching saves time and space than linear one.












