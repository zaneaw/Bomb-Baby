# Explanation

I first 'solved' this problem by implementing a Breadth-First Search Algorithm. I quickly realized that when the results have the potential to be 10^50, or 1 with 50 zero's behind it. So I had to hit the drawing board and solve this with some outside-of-the-box thinking!

I recognized pretty fast that I needed to work backward to solve this problem. I tried to use a simple subtraction method, but upon further testing, realized that it wouldn't be possible if the inputs were too far apart. Something like 10 with 50 zero's behind it and 1 being subtracted down to an answer... Not going to work!

Then it hit me, I had to divide it! And that was great because it drastically cut down on the runtime, no matter how large the numbers were or how far apart they were. There was still an issue here though! There was no way to track the partial 'cycles'. That's where the Modulo Operator comes into play. This is a really simple Python function but it was that special, final ingredient for me to solve this!


**Voila! Problem solved!**


So let me explain the code a little bit with an example.
Let's take 961 Mach Bombs and only 25 Facula Bombs. Plugged into the code it would look like:
```
# Input
solution(961, 25)

# Output
45
```
_I should note that it does not matter if 961 Bombs are Mach or Facula - the code sorts them into 'x' and 'y' based on which one is larger and which one is smaller._

Let's check out what's going on behind the scenes. First, the code does some simple checks for the input numbers to know if it should return impossible or not. If it passes that case, we move onto the most important part of the code. Remember, we are going to iterate backwards essentially, starting from the max input. We are going to divide the larger input by the smaller input until we reach 0 or it triggers the 'impossible' logic case.

For our example, at the start:  
```
x = 25
y = 961
961 / 25 = 38.44 -> converted to an int -> 38 = p1
961 % 25 = 11    ->    already an int   -> 11 = p2
# logic check here to return impossible if need be
# 'cycles' now ticks up by the value in p1
```
In other words, _38_ cycles _( p1 )_ had to pass for 25 _(x)_ to equal 950 with _11_ remaining _( p2 )_.
```
y = x         # y = 25
x = p2        # x = 11
# check if we are ready to return the answer
```
The value stored in _y_ is no longer needed but _x_ and _p2_ are values that we still need, so the value of _x_ overrides the value stored in _y_ and _x_ is then overridden by _p2_. Now we loop back around and go again, just with new values this time.
```
x = 11
y = 25
25 / 11 = 2.273 -> converted to an int -> 2 = p1
25 % 11 = 3     ->    already an int   -> 3 = p2
# logic checks again
# 'cycles' goes up 2
# check again if we are ready to return the answer
y = x         # y = 11
x = p2        # x = 3
```
Just like that, we are already at **40** cycles!  
Now, the rest of the example would look a little like this:
```
x = 3
y = 11

11 / 3 = 3 = p1
11 % 3 = 2 = p2

cycles + 3 = 43
```
Next:
```
x = 2
y = 3

3 / 2 = 1
3 % 2 = 1

cycles + 1 = 44
```
Next:
```
x = 1
y = 1

1 / 1 = 1
1 % 1 = 0

cycles + 1 = 45
```
Finally:
```
x = 0
y = 1
if x == 0 and y == 1: This line results in being True so the return statement is executed
```
The logic check of x being equal to 0 and y equal to 1 triggers! We've gotten to the end and we have an answer. Finally, let's return the answer, _*as a string like requested_.

```
Return str(cycles)
```
