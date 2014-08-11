Title: How Python executes your code
Date: 2014-08-05
Slug: how-python-executes-code
Status: draft

This post will give a brief overview of what's actually happening when Python
executes your code. This is a very broad topic and it can be approached from
many directions, but we won't go below C level, meaning this post won't go
into assembly language and how things are working on a system level. Also,
this only applies to default Python implementation, CPython.

## Bytecode

Even though Python is an interpreted language, there is still some compilation
going on - Python code is compiled into bytecode. That bytecode is then being
executed (or interpreted) by Python virtual machine.

To see the bytecode for any Python function, you can use dis module.

    :::python
    import dis

    def add(a, b):
        return a + b

    dis.dis(add)

    # Output:
    2           0 LOAD_FAST                0 (a)
                3 LOAD_FAST                1 (b)
                6 BINARY_ADD
                7 RETURN_VALUE


* explain above output

* how many bytecodes and where are they defined

* where is the main loop that executes bytecode

* where is the C code
