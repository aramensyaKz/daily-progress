# Meaningful commits

A useful commit should leave the repository in a coherent state and explain one
complete idea. A good daily-progress entry therefore answers three questions:

1. What was explored or changed?
2. What concrete result was produced?
3. How was the result checked?

## When to split work

Split changes when they can be reviewed independently. For example, a small
tool, its tests, and its usage documentation can be separate commits because
each has a distinct purpose. Do not split formatting changes or individual
sentences merely to increase the commit count.

## Commit message pattern

Use an imperative subject with a clear scope:

```text
docs: explain meaningful commit boundaries
feat: add journal entry generator
test: cover journal entry validation
```

This makes the history readable and turns the contribution graph into a record
of actual progress rather than an activity counter.
