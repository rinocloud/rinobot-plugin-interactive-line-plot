import sys
import os
import numpy as np
import warnings
from bokeh.models import Tool, BoxZoomTool, PanTool, WheelZoomTool, ResetTool
from bokeh.plotting import figure, output_file, save

Set3_12 = ['#a6cee3','#1f78b4','#b2df8a','#33a02c','#fb9a99','#e31a1c','#fdbf6f','#ff7f00','#cab2d6','#6a3d9a','#ffff99','#b15928']


class CustomSaveTool(Tool):
    __implementation__ = open(os.path.join(os.path.dirname(__file__), "custom_save.coffee")).read()


def load(fpath, skiprows=0):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            return np.loadtxt(fpath, skiprows=skiprows)
        except ValueError:
            return load(fpath, skiprows+1)
        except StopIteration:
            return []


def main(filepath):
    # read and setup data
    filename_without_ext = os.path.splitext(filepath)[0]
    data = load(filepath)
    x = data[:, 0]
    y = data[:, 1:]

    # setup plot colors and styles
    palette = Set3_12
    plot_styles = {
        "line_width": 2,
        "line_color": palette[0],
        "line_alpha": 0.7
    }

    # create the plot
    tools = [
        CustomSaveTool(),
        'box_zoom',
        PanTool(),
        WheelZoomTool(),
        ResetTool()
    ]

    p = figure(
        webgl=True,
        x_axis_label='x',
        y_axis_label='y',
        tools=tools,
        active_drag='box_zoom'
    )

    # loop over each y column and plot
    for index, yi in enumerate(y.T):
        plot_styles["line_color"] = palette[index % len(palette)]

        # change the plot style for every second and third graph
        # just to make things interesting
        if index % 3 == 0:
            p.line(x, yi, **plot_styles)
            p.circle(x, yi, fill_color= None, **plot_styles)
        elif index % 2 == 0:
            p.line(x, yi, **plot_styles)
        else:
            p.line(x, yi, **plot_styles)
            p.square(x, yi, fill_color= None, **plot_styles)

    # output to html file
    p.plot_height=600
    p.plot_width=1000
    output_file(
        filename_without_ext + '.html',
        title=filename_without_ext + '.html',
        mode='inline'
    )
    save(p)


# if this is run from the command line then run the
# main function
if __name__ == "__main__":
    main(sys.argv[1])
