# CMPS 2200 Assignment 2

**Name:**Marco Carbullido

In this assignment we'll work on applying the methods we've learned to analyze recurrences, and also see their behavior
in practice. As with previous
assignments, some of of your answers will go in `main.py`.. You
should feel free to edit this file with your answers; for handwritten
work please scan your work and submit a PDF titled `assignment-02.pdf`
and push to your github repository.


1. Derive asymptotic upper bounds of work for each recurrence below.
  * $W(n)=2W(n/3)+1$
.  
.  Because $d = 0 < \log_3(2)$, we can obtain upper bounds with $O(n^{\log_3(2)})$
.  
.  
  * $W(n)=5W(n/4)+n$
.  
.  Because $d = 1 < \log_3(2)$, we can obtain upper bounds with $O(n^{\log_4(5)})$
.  
  * $W(n)=7W(n/7)+n$
.  
.  Because $d = 1 = \log_7(7)$, we can obtain upper bounds with $O(n{\log_7(n)})$
.  
.  
  * $W(n)=9W(n/3)+n^2$
.  
.  Same as above, $d = 2 = \log_3(9)$, we get $O(n^2{\log_3(n)})$
.  
.  
.  
  * $W(n)=8W(n/2)+n^3$
.  
.  Same as above, $d = 3 = \log_7(7)$, we get $O(n^3{\log_2(n)})$
.  
.  
.  
  * $W(n)=49W(n/25)+n^{3/2}\log n$
.  
.  We can deduce this is root dominated and this the $n^{3/2}\log n$ term dominates. Thus, it is bounded by $O(n^{3/2}\log n)$
.  
.  
.  
  * $W(n)=W(n-1)+2$
.  
.  This is, in the worst case, going to repeat n times, so the runtime upper bound is O(n)
.  
.  
.  
  * $W(n)= W(n-1)+n^c$, with $c\geq 1$
.  
.  We get O(n^c+1)
.  
.  
  * $W(n)=W(\sqrt{n})+1$
.  With additional cost of 1 at each level, and the recurrence continuing until there is one element in the node, this process can repeat 1/2^i times.
.  Using this logic, n^(1/2^i) = 1, which gives us i = log(log(n)). Thus, we must incur 1 unit work log(log(n)) times, so we get O(log(log)n)
.  
.  


2. Suppose that for a given task you are choosing between the following three algorithms:

  * Algorithm $\mathcal{A}$ solves problems by dividing them into
      five subproblems of half the size, recursively solving each
      subproblem, and then combining the solutions in linear time.
    
  * Algorithm $\mathcal{B}$ solves problems of size $n$ by
      recursively solving two subproblems of size $n-1$ and then
      combining the solutions in constant time.
    
  * Algorithm $\mathcal{C}$ solves problems of size $n$ by dividing
      them into nine subproblems of size $n/3$, recursively solving
      each subproblem, and then combining the solutions in $O(n^2)$
      time.

    What are the asymptotic running times of each of these algorithms?
    Which algorithm would you choose?

    A: runtime is bounded by O(n^log_2 (5))
    B: runtime is bounded by O(n)
    C: runtime is bounded by O(n^2)
    Thus, we would choose algorithm B, belonging to the most scalable runtime.


3. Now that you have some practice solving recurrences, let's work on
  implementing some algorithms. In lecture we discussed a divide and
  conquer algorithm for integer multiplication. This algorithm takes
  as input two $n$-bit strings $x = \langle x_L, x_R\rangle$ and
  $y=\langle y_L, y_R\rangle$ and computes the product $xy$ by using
  the fact that $xy = 2^{n/2}x_Ly_L + 2^{n/2}(x_Ly_R+x_Ry_L) +
  x_Ry_R.$ Use the
  stub functions in `main.py` to implement Karatsaba-Ofman algorithm algorithm for integer
  multiplication: a divide and conquer algorithm that runs in
  subquadratic time. Then test the empirical running times across a
  variety of inputs to test whether your code scales in the manner
  described by the asymptotic runtime. Please refer to Recitation 3 for some basic implementations, and Eqs (7) and (8) in the slides https://github.com/allan-tulane/cmps2200-slides/blob/main/module-02-recurrences/recurrences-integer-multiplication.ipynb
 
 


