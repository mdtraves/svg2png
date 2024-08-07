import sys
import cairosvg

def convert_svg_to_png(svg_name, height):
  """Converts an SVG to PNG with specified height.

  Args:
    svg_name: The name of the SVG file (without extension).
    height: The desired height of the output PNG image.
  """

  svg_file = f'./svg/{svg_name}.svg'
  png_file = f'./png/{svg_name}.png'

  cairosvg.svg2png(url=svg_file, write_to=png_file, output_height=height)

  print(f'SVG "{svg_name}" successfully converted to PNG')

# Access command-line arguments
if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("Usage: python index.py <svg_name> <height>")
    sys.exit(1)

  svg_name = sys.argv[1]
  height = int(sys.argv[2])  # Convert height argument to integer

  convert_svg_to_png(svg_name, height)
