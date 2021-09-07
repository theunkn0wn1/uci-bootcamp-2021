# Import this

Now that we have covered [modules](modules.md) and [packages](packages.md), we can finally talk
about `libraries` and how to `import` them.

So what is this `import` you speak so highly of?

In python, the `import` keyword allows us to bring names into scope from another `module` or `package`.

```python
# Standard library components are, by style, listed first.
import io

# Note: Many of the Scientific Computing Python libraries tend to shorthand 
#       their module names. The following imports follow their convention, 
#       to be consistent with their documentation and examples.
import pandas as pd
import numpy as np

# In This case, we import a specific name from a package instead of the entire package.
from matplotlib import pyplot as plt
```

# Libraries

The organization of code into *modules*, which are organized into *packages* forms the backbones of
what we call `Libraries`. Libraries are *packages* that share a common goal: such as providing
filesystem abstractions like `Pathlib` does, or focus on plotting scientific data like `matplotlib`
does.

The ability to `import` code written somewhere else by potentially other people is what forms the
foundation for Python's various communities and the language's wide range of applications.

In the next section, we will cover some of the more important libraries as it relates to scientific
computing, plus some tools that will make writing maintainable Python easier.