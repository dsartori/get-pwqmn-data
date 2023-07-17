import matplotlib.pyplot as pyplot
import matplotlib.dates as mdates

def generate(dimensions, values, series, seriesDescription, filename):
	pyplot.rcParams.update({'font.size':6})
	# set up chart sub components
	fig, ax = pyplot.subplots()

	# tick and axis parameters
	ax.tick_params(axis='x',rotation=50)
	ax.set(xlabel = 'date',ylabel = series)

	# chart title
	ax.set_title(seriesDescription,loc='center',wrap=True)

	# generate and save chart
	ax.plot (dimensions, values)
	ax.grid()
	fig.savefig(filename)

	# close the chart
	pyplot.close(fig)
