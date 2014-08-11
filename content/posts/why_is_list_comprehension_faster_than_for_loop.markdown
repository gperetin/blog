Title: Why is list comprehension faster than for loop in Python
Date: 2014-08-05
Slug: list-comprehension-vs-for-loop
Status: draft


Have you ever wondered why are list comprehensions faster than for loops? This
post will try to explain what is going on when Python executes your for loops
and list comprehensions and what can you do to speed it up.

Note: this post describes behaviour of Python 2.x, it has been slightly
changed in Python 3, perhaps a topic for another blog post :)

Consider these 2 simple benchmarks:

    :::python
    # List comprehension
    def lc():
        return [i for i in range(10000)]

    
    # For lopp
    def loop():
        nums = []
        for i in range(10000):
            nums.append(i)
        return nums

If we run them via IPython's magic %timeit, we get these results:

    :::python
    %timeit lc()
    1000 loops, best of 3: 387 µs per loop

    %timeit loop()
    1000 loops, best of 3: 876 µs per loop

No matter how big range do you use, list comprehension is approximately 2
times faster. The answer lies in the way the element is actually added to the
list, and to see that we need to dive in Python bytecode.

## Bytecode

Bytecode is an intermediary representation of your program. When you run your
program, Python compiles it to bytecode, which is then being executed by
Python virtual machine. We can inspect the bytecode for our `loop()` function
above by running this command:

    >>> loop.func_code.co_code
    'g\x00\x00}\x00\x00x!\x00t\x00\x00d\x01\x00\x83\x01\x00D]\x13\x00}\x01\x00|\x00\x00j\x01\x00|\x01\x00\x83\x01\x00\x01q\x13\x00W|\x00\x00S'

Since this is not really useful, Python comes with a module called `dis` that
prints bytecode in a bit more user-friendly format.

    :::python
    import dis
    dis.dis(loop)

      2           0 BUILD_LIST               0
                  3 STORE_FAST               0 (nums)

      3           6 SETUP_LOOP              33 (to 42)
                  9 LOAD_GLOBAL              0 (range)
                 12 LOAD_CONST               1 (10000)
                 15 CALL_FUNCTION            1
                 18 GET_ITER
            >>   19 FOR_ITER                19 (to 41)
                 22 STORE_FAST               1 (i)

      4          25 LOAD_FAST                0 (nums)
                 28 LOAD_ATTR                1 (append)
                 31 LOAD_FAST                1 (i)
                 34 CALL_FUNCTION            1
                 37 POP_TOP
                 38 JUMP_ABSOLUTE           19
            >>   41 POP_BLOCK

      5     >>   42 LOAD_FAST                0 (nums)
                 45 RETURN_VALUE

Above output has 5 columns; first is the line number of code that generated
this portion of the bytecode, relative to the start of the function. Second
is bytecode offset, we won't be interested in this one, just not that it's
either either each instruction is either 3 bytes long (if it takes an
argument) or 1 byte (if it takes not arguments). Third column is the name
of the instruction. Each instruction is identified by it's opcode, which is
a regular (small) integer. Python 2.7.8 has 110 instructions and if you're
interested in these, check out the `Include/opcode.h` in Python source code.
Fourth column is an argument to an opcode, and fifth column is an explanation
of what the argument means (it's value, name of the function or variable, etc.)

We won't go line by line throught this output, the part we are interested in is
at byte offsets 22-34, which corresponds to the body of the for loop.

* inspect lc bytecode
* inspect loop bytecode

* make a simple C file that calls both PyList_Append and call_function
