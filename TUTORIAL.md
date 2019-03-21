# Continuous integration tutorial

This tutorial presents how to use continuous integration (CI) in a Python code development, using the [pytest](https://docs.pytest.org/en/latest/contents.html) and [Travis](https://travis-ci.com).
Through a few simple exercises, you'll go through different features of CI.

## pytest module of Python

[pytest](https://docs.pytest.org/en/latest/contents.html) is a framework that makes building simple and scalable tests easy.

You can install it using pip (`pip install -U pytest`) or in a conda environment (`conda install pytest`).
You can run pytest within a terminal (linux and osx) or in the anaconda prompt (Windows).

## Exercise 0: Hello World!
In this exercise, you will write a first test in a file `test_hello_world.py`.
* In a file `test_hello_world.py`, write a python function that prints "Hello World!" and returns 0.
* In that same file, write a new function `test_hello_world()` that call your hello world function and asserts that it returned 0.
* Test your file running `pytest test_hello_world.py`.
* Questions:
  * What happens if you run `pytest .` ?
  * And if you rename the file `test_hello_world.py` to `hello_world.py` ?
  * And if you rename the functions ?
  
## Exercise 1: The Fibonacci sequence
The [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) is a sequence of natural numbers where each number
is the sum of the two previous numbers in the sequence, starting by 0 and 1:
```
F[0] = 0
F[1] = 1
F[n] = F[n-1] + F[n-2]
```
* In a file `fibonacci.py`, write a function that returns the n th Fibonacci number.
* In a file `test_fibonacci.py`, write a function `test_fibonacci()` that asserts the 5th Fibonacci number is a positive natural number.
* Modify `test_fibonacci()` to `test_fibonacci(n)` that checks the `n` th Fibonacci number, and test it for different values of `n`.
  * You'll need to use `@pytest.mark.parametrize('n', [0, 1, 5, -1])` as a decorator to your function.
  * What happens for a negative parameter n ?
  
## Exercise 2: The Fibonacci sequence revisited
* You now want to write a function `strict_fibonacci(n)` that raises an error if parameter `n` is not a natural number.
* You can also test this function, checking that it raises an error as expected for negative `n`:
  * You'll need to use such decorator: `@pytest.mark.parametrize('n', [1, pytest.param(-1, marks=pytest.mark.xfail(strict=True))])`

## Using github and Travis
Using Travis CI, you can automatically test every commit you push on github. 
### How to get started with Travis (see more info in the [Travis tutorial](https://docs.travis-ci.com/user/tutorial/))?
 * Go to Travis-ci.com and Sign up with GitHub.
 * Accept the Authorization of Travis CI. You’ll be redirected to GitHub.
 * Click the green Activate button, and select the repositories you want to use with Travis CI.
 * Add a .travis.yml file to your repository to tell Travis CI what to do.
   * Travis can test your code using different versions of Python.
     See this example of [.travis.yml](https://github.com/OceanParcels/continuous_integration_example/blob/master/travis.yml.simple)
   * Testing Python under OSX is currently broken. You can't do it as for the linux example above, but you can still
     test an OSX Python by installing it with conda. To use any conda environment, you can also use such approach, with this
     [.travis.yml](https://github.com/OceanParcels/continuous_integration_example/blob/master/.travis.yml)
 * Now, each time you'll push a commit on github, your full code will be tested.
 * You can setup Travis in your settings to only test master branch, every branch, the pull requests, etc.
 
### The AppVeyor CI tool
To test your code on Windows, you can use [AppVeyor](https://www.appveyor.com), which is similar to Travis.
