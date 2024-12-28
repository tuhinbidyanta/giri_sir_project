
import pygmt

def plot_imag(path):

    fig = pygmt.Figure()

    region = [68, 97, 8, 38]
    fig.basemap(region=region, projection="M6i", frame=True)
    fig.image(imagefile =path ,position=f"g{region[0]}/{region[1]}+w6i")
    fig.show()
