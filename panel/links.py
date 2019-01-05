"""
"""
import param

from holoviews.plotting.links import Link


class RangeAxesLink(Link):
    """
    The RangeAxesLink sets up a link between the axes of the source
    plot and the axes on the target plot. By default it will
    link along the x-axis but using the axes parameter both axes may
    be linked to the tool.
    """

    axes = param.ListSelector(default=['x', 'y'], objects=['x', 'y'], doc="""
        Which axes to link the tool to.""")


class RangeAxesLinkCallback(param.Parameterized):
    """
    Links source plot axes to the specified axes on the target plot
    """

    def __init__(self, root_model, link, source_plot, target_plot):
        if target_plot is None:
            return
        if 'x' in link.axes:
            target_plot.handles['plot'].x_range = source_plot.handles['plot'].x_range
        if 'y' in link.axes:
            target_plot.handles['plot'].y_range = source_plot.handles['plot'].y_range


RangeAxesLink.register_callback(backend='bokeh',
                                callback = RangeAxesLinkCallback)
