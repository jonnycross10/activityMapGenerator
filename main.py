from cairosvg import svg2png
from svgFile import svg


img = "https://ghchart.rshah.org/jonnycross10.svg"


svg2png(url= img, write_to='output.png')



