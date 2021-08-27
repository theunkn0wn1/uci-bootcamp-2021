# The Set

The `set`, AKA a `hashset`, is a unordered, resizable, heterogenous data structure that has the
properties of a [Discrete mathmatics Set](http://discrete.openmathbooks.org/dmoi3/sec_intro-sets.html).

- All items of a set are [`Hashable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable)
- All items of a set are unique, based on their hash.
- The intersection, union, disjunction, etc can be taken between Sets.
- `Contains` checks against a set are O(1), which can make them quite fast.
- Insertions are idempotent, as all items are unique.