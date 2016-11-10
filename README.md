# rinobot-interactive-line-plot

> [Live example link](https://rawgit.com/rinocloud/rinobot-plugin-interactive-line-plot/master/examples/data-int-line-plot.html)

Makes an interactive line plot of xy or xyyy data.

So if your data has many columns, this package will take  the
first column as the x axis, and each subsequent column as
different y plots.

If your data looks like

```
0.0 8.7
1.4 2.4
2.4 2.3
3.3 3.5
4.1 7.3
...
...
```

If will make an interactive html graph like:

## Options:

In the extra args section of the rinobot automation config you can set the following parameters

- xlabel: the label for the x axis
- ylabel: the label for the y axis
