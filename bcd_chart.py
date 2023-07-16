import matplotlib.pyplot as pyplot
import matplotlib.dates as mdates

def generate(dimensions, values, series, seriesDescription, filename):
	pyplot.rcParams.update({'font.size':6})
	# set up chart sub components
	fig, ax = pyplot.subplots()

	# tick and axis parameters
	ax.tick_params(axis='x',rotation=50)
	ax.set(xlabel = 'date',ylabel = series)
	ax.xaxis.set_major_locator(pyplot.MaxNLocator(25))
	ax.yaxis.set_major_locator(pyplot.MaxNLocator(20))

	# chart title
	ax.set_title(seriesDescription,loc='center',wrap=True)

	# generate and save chart
	ax.plot (dimensions, values)
	ax.grid()
	fig.savefig(filename)

