---
title: "Using Microsoft python-type-stubs with Pyright"
layout: single
excerpt: "For better type checking and completion."
categories:
  - technical
---

Python type annotations allow static type checking, so that you can catch obvious `AttributeError: NoneType object has no attribute ...` in your editor.
They also allow better code completion, because in many cases, type checking tools can infer the type of the object based on return type annotations of functions or methods.
However, not all libraries (especially the ones that were created before Python type annotation got established) have type annotations.

That's why *type stubs* exist.
They have `.pyi` extensions and are like C headers, which only declare class, function, or method names and their parameter types without implementation.
These type stubs do not have to be coupled with the actual library.
So virtually anyone can just create type stubs for an existing library and ship it separately.

Microsoft's `pylance` ships with type stubs bundled for popular libraries without native type annotations.
But especially for large libraries type stubs cannot be perfect, so they have a repository called [`python-type-stubs`](https://github.com/microsoft/python-type-stubs) to collaboratively work on creating type stubs together with the community, and these stubs are bundled together with `pylance`.

However, `pylance` is closed source, and is only available inside VS Code.
As a Neovim person, I instead have to use the open-source version of `pylance`, which is [`pyright`](https://github.com/microsoft/pyright).
However, by default, `pyright` doesn't ship with `pylance`'s type stubs.

So the question is, **how do I use `python-type-stubs` with `pyright`**?
It's actually simple enough, but at the time of writing, it seems like nowhere on the Internet just has a straightforward guide on this.

Say you have a Python project `proj` managed with `git`.

Add `python-type-stubs` as a git submodule under the directory `stubs`:
```console
$ cd proj
# Assuming you have GitHub SSH authentication set up.
$ git submodule add git@github.com:microsoft/python-type-stubs stubs
```

Then, point `pyright` to the stubs inside the submodule.

If you're using `pyproject.toml`:
```toml
[tool.pyright]
stubPath = "./stubs/stubs"
```

If you're *not* using `pyproject.toml`, you need to have `pyrightconfig.json` in the root of your workspace:
```json
{
    "stubPath": "./stubs/stubs"
}
```

When you see glitches in the type stubs provided by `python-type-stubs`, just post a PR fixing the issue.
When the PR gets merged, update the submodule (e.g., `git submodule update`).
