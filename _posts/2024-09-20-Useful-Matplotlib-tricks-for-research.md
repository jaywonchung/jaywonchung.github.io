---
title: "Useful Matplotlib Tricks for Research"
layout: single
excerpt: "All about reducing headaches and mistakes."
categories:
  - research
  - technical
---

I believe Matplotlib is the de facto standard for plotting.
Because it's entirely Python code, it's reproducible (given the same input data), easy to version control, and easy to generate and iterate with ChatGPT.

I'll go over a couple tricks with Matplotlib that I've found useful, especially for research.

## Making plots compatible with PowerPoint

PNG files exported with Matplotlib don't look very nice in PowerPoint slides, especially when you enlarge it.
Also, you can't, say, change the color of your lines or remove unnecessary components, because they're all flattened into an image file.

Instead, export your plot in SVG as well.
All you need to do is call `fig.savefig` once more with a file path that ends with `.svg`.
Then, drag the SVG file onto PowerPoint, right click, and click *Convert to Shape*.
Now, every component (e.g., line, text) will be converted to PowerPoint-native objects that you can tweak freely.
See also [Microsoft's documentation](https://support.microsoft.com/en-us/office/edit-svg-images-in-microsoft-365-69f29d39-194a-4072-8c35-dbe5e7ea528c) on this.

Before you actually call `savefig`, make sure you have the following configuration:

```python
import matplotlib as mpl
mpl.rcParams["svg.fonttype"] = "none"
```

Without this, every *character* in your plot will be saved as a separate text box.
That's beyond annoying.

## Making plot files Git-friendly

Let's say you're exporting your plot in PDF or SVG and committing it into a Git repository for paper-writing.
Normally, if you re-export the exact same plot (e.g., because you had to restart and re-run every Jupyter Notebook cell), `git` will recognize them as modified.
This is because by default, the contents of the PDF/SVG file will change slightly.
This is particularly bad for PDF files, because they are binaries -- `git` will have to store the whole PDF file because it doesn't know how to do line-level diff on binary files.
However, it is possible to make Matplotlib generate the *exact* same file each time deterministically.

### PDF files

```python
fig.savefig("plot.pdf", metadata={"CreationDate": None})
```

Notice that we're removing the file creation date from the PDF metadata.

### SVG files

```python
fig.savefig("plot.svg", metadata={"Date": None}, **kwargs)
```

The `savefig` call is basically the same for SVG, except that it needs a slightly different metadata key for the creation date.
However, we do need one more thing *before* we call `savefig`:

```python
import matplotlib as mpl
mpl.rcParams["svg.hashsalt"] = "42"
```

Without fixing the hash salt, SVG generation is non-deterministic and `git` will (rightfully) detect the file as modified.

## Avoiding Type 3 fonts

This may not apply to all publishers, but at least USENIX and ACM papers require final PDFs to not have any *Type 3* fonts.
They just want *Type 1* fonts.
So, when we export our plots into PDF files and embed them into our LaTeX document, it's better to make sure they don't contain any Type 3 fonts in the first place.

```python
import matplotlib as mpl
mpl.rcParams["pdf.fonttype"] = "42"
mpl.rcParams["ps.fonttype"] = "42"
```

Unlike `svg.hashsalt` where 42 was just a random number, 42 for the font type actually means TrueType fonts.
The default is 3, which means Type 3 fonts.

## An `mplstyle` file

You will definitely forget all of these next time.
Instead of trying to remember, put everything in a style file like this (call it something like `paper.mplstyle`):

```
# Fonts
font.size : 9

# SVG export now doesn't render font as path, but saves fonts as text objects.
# This allows for easier integration with MS Office.
svg.fonttype : none
# Make SVG generation deterministic
svg.hashsalt : 42

# Avoid type 3 font usage
pdf.fonttype : 42
ps.fonttype : 42
```

Then, import the file with a one-liner:

```python
import matplotlib.pyplot as plt
plt.style.use("./paper.mplstyle")
```
