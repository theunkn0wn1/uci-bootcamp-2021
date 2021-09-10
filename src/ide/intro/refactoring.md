# Refactoring

As the size of code grows, so does the understanding of the developer. What may have made sense at the
start of the project may suddenly not work quite as well halfway in.

Sometimes functions simply need to be moved into a new module for better organization, or a repeated
operation simplified into a variable. Sometimes Entire superclasses can be extracted to better
represent the code structure.

These are all examples of `refactoring`
> Refactor: To rewrite existing source code in order to improve its readability, reusability and/or structure, without changing the behavior of the code.


Let's take this presentation, for example!

At the time of writing, the IDE documents are full of images, which are included in the rendered
documents.

Initially, all of the images sat at the same level as the source `.md` documents they are included in,
which are all in the same `src/ide` folder. This proved itself unwieldy, as the file structure is not
conducive to a viewer's understanding of what documents import which image files.

## Moving files

One mode of refactoring is to move files from one directory to another.

> "Why does the IDE need to support this? can't you just move it in the OSes file browser?"
Well no, because the files are referenced by *other files*. Moving a file without modifying its uses will break those uses. 

Pycharm supports many forms of refactoring which are valid in different contexts.
In this specific case, files can be moved via the projects window.

From the context menu (right-click on the file), select refactor>move

Further reading [Move Refactorings official docs](https://www.jetbrains.com/help/pycharm/move-refactorings.html)