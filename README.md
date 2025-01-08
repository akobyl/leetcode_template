# Leetcode Programming Interview Practice Template

Practicing for programming interviews is easier if we have a system in place that can:

* Step through and debug problems quickly
* Add test cases easily
* Run tests automatically
* Have built-in modules for the common Binary Tree and List Node problems
* Be able to revisit old problems and run them again!

This template uses [uv](https://docs.astral.sh/uv/) to set up a virtual environment and run pytest.

## Doing leetcode problems

Python is the lingua franca of programming interviews, so this template focuses on a Python.  Generally you don't really want to use any external libraries in interviews, so those are not included here.

When solving problems, it helps to be able to add a thought process at the start!  This helps when you want to revisit it in the future, whether that is in a few weeks or in a few years.  A simple comment block helps.

I prefer to name the problems with the number and the difficulty level so they are easy to sort and find, e.g. `0001_E_two_sum.py`.  Shockingly there are over 3,000 leetcode problems at the time of this writing, so I use 4 digits and 0-pad the file name.

For Trees, the example problem here should show how we can copy in the test cases straight from leetcode.com and have a correct structure.  Printing the tree can help with visual debugging.

## Running tests

To execute the tests, run `uv run pytest` in the root directory.

```
❯ uv run pytest
=================== test session starts ===================
platform linux -- Python 3.11.11, pytest-8.3.4, pluggy-1.5.0
rootdir: /home/andy/dev/leetcode_template
configfile: pyproject.toml
collected 7 items

0002_M_add_two_numbers.py ...                       [ 42%]
0098_M_validate_binary_search_tree.py ..            [ 71%]
1257_M_smallest_region.py ..                        [100%]

==================== 7 passed in 0.01s ====================
```
