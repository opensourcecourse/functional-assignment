# Functional Assignment

Just like object-oriented programming, functional programming is 
a huge topic which we are only going to approach tangentially. Rather
than learning functional programming in the abstract, (which python is
arguably not a good fit for anyway) we are going to practice
using some of python's functional features.


## Task 1: Function registration (5 points)

Look at task_1.py and fill in the implementation. Running test_task_1.py will
let you know if it is correct.

## Task 2: Decorative logging (5 points)

Open task_2.py and fill in the implementation. Use test_task_2.py to check
your work.

## Task 3: Simple DataClasses (5 points)

Take a look at python's [data classes](https://docs.python.org/3/library/dataclasses.html).
They are an excellent option for making basic data containers and even offer (shallow)
immutability. Next, open task_3.py and create a simple dataclass.

## Task 4: Recursive Rascality (10 points)

One natural fit for recursion is parsing tree or graph-like data structures. 
Here we will traverse a [truncated family tree](https://webtreeprint.com/tp_famous_gedcoms.php)
of several famous American politicians.

Take a look at task_4.py and fill in the implementation for `count_people`.
This function's docstring describes its behavior. 

Note: recursion is not always a good fit for tree/graph traversal, especially when
breadth first search is the best option, as in finding the shortest path between
two nodes. In the latter case a queue structure is a more natural fit but not in the scope
of this assignment.
