# A crash course in Python, plus data science

This repository contains [sample code](uci_bootcamp_2021/examples) as well as the [presentation slides](./src/SUMMARY.md) for the [`UCI PSML 2021 Bootcamp presentation: Python for Data Science`](https://ps.uci.edu/psml/node/63)

Note: while the `.md` documents used to prepare the slides can be read directly from Github, to get the full experience build the book.

## Building the book
The book is built using [`rust-mdbook`](https://github.com/rust-lang/mdBook), so you will need [Rust](https://www.rust-lang.org/) installed to install and run that.

```bash
gh clone theunkn0wn1/uci-bootcamp-2021
cd uci-bootcamp-2021
mdbook serve
```