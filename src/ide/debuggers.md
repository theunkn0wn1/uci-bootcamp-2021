# Debuggers

As you write more and more complex code, it is often times necessary to emit diagnostic information in
the middle of the program.

For instance, you might want to spot-check the algorithm by emiting an intermediate result from a
larger computation. Another case is in a large server application, and something is not behaving as
anticipated, so you need to know what the program thinks its doing.

> Computers arn't smart: they do exactly what we tell them to do, not what we intended to tell them to do.

## Methods of debugging: logging

A common strategy to diagnosing misbehaving code is to add diagnostic output. In other words, modifying
the source code of the program to emit *logging* messages.

> Side note: in simple cases `print` / `std::cout <<` / `System.out.println` / etc are usable; but suffer from two key flaws:
>  1. Not every type can be trivially cast to a string and printed.
>  2. Once debugging is complete and the bug is fixed; all of that output has to be removed.
>
> The best practice when adding logging to a project, is to use a *logging framework*.

## Methods of debugging: attaching a debugger

The logging method requires source code modification, which is quite unwieldy. It becomes infeasable
when the bug is either non-trivial or otherwise expensive to reproduce.

- Debuggers require **no code modification**, and can frequently be attached to running programs.
- They can inspect the memory of the process, revealing what the program is actually doing.
- Limited code execution features

Debuggers can be extremely powerful once mastered.

Of course, an IDE's debugger window can be daunting to look at to the untrained eye. This page aims to
demystify the Jetbrain's PyCharm Debugger.

> Side Note: Most of the debugger concepts translate both to other IDEs in the Jetbrains family, and to other unrelated IDEs.

## Debugging a program in PyCharm

The first thing you need to debug a script written in Python, using PyCharm, is a [run configuration]()
.

For this page, we will be using the [pathlib example](../python/pathlib.md) run config established in
the [run configurations]() section.

