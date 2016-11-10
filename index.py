import rinobot_plugin as bot
import numpy as np
import os
from bokeh.models import Tool, BoxZoomTool, PanTool, WheelZoomTool, ResetTool
from bokeh.plotting import figure, output_file, save

class CustomSaveTool(Tool):
    __implementation__ = open(os.path.join(os.path.dirname(__file__), "custom_save.coffee")).read()

def main():
    filepath = bot.filepath()
    xlabel = bot.get_arg('xlabel', type=str)
    ylabel = bot.get_arg('ylabel', type=str)

    data = bot.loadfile(filepath)
    x = data[:, 0]
    y = data[:, 1:]

    palette = ['#a6cee3','#1f78b4','#b2df8a','#33a02c','#fb9a99','#e31a1c','#fdbf6f','#ff7f00','#cab2d6','#6a3d9a','#ffff99','#b15928']
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
        x_axis_label=xlabel,
        y_axis_label=ylabel,
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

    outname = bot.no_extension() + '-int-line-plot.html'
    outpath = bot.output_filepath(outname)

    output_file(outpath, title=outname, mode='inline')
    save(p)


if __name__ == "__main__":
    main()
