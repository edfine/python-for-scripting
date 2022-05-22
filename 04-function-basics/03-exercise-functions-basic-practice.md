# Exercise: Using Functions

This exercise is meant to help you practice:

* Creating and calling functions.

# The Exercise

You will be writing a python script that creates functions then uses those functions.

> Hint: some of Python's built in functions may help you write this code faster. See: [https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)

To practice creating and using standalone functions write the following two functions. Make sure to test each one by creating input and checking that it's output is what you expect.

### Mean

Create a function called mean that accepts a list of numbers and returns the mean of those numbers. Remember, the mean is the sum of the values divided by the number of values. 

You should be able to use your function like this:

```python
numbers = [5, 10, 15]
m = mean(numbers)
print(m) # 10
```

**Be sure to test your code with more than just this single test case!**

> Hint: consider using the `sum` and `len` built in functions...

### Median

Create a function called median that accepts a list of numbers and returns the median of those numbers. Remember, the median is the value at the center of the sorted dataset. If there are an even number of values in the dataset the median is the mean of the two center values.

You should be able to use your function like this:

```python
numbers = [5, 10, 15]
m = median(numbers)
print(m) # 10
```

**Be sure to test your code with more than just this single test case!**

> Hint: Consider using the `sorted` built in function.
> Hint: You can determine if a list has an even number of items with `is_even = len(numbers) % 2 == 0`. See: [The modulo operator](https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/)