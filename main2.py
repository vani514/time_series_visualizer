from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

# Generate and save plots
line_fig = draw_line_plot()
line_fig.savefig("line_plot.png")

bar_fig = draw_bar_plot()
bar_fig.savefig("bar_plot.png")

box_fig = draw_box_plot()
box_fig.savefig("box_plot.png")

print("Plots saved as 'line_plot.png', 'bar_plot.png', and 'box_plot.png'")
