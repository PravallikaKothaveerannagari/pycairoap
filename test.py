import os

import cairo

# =============== Create surface and context =============== #

# `cairo.ImageSurface(format, width, height)` provides the ability to render to 
#   memory buffers either allocated by cairo or by the calling code.
WIDTH, HEIGHT = 256, 256
sfc = cairo.ImageSurface(cairo.Format.ARGB32, WIDTH, HEIGHT)
# ^^^ You can also replace `cairo.Format.ARGB32` to `cairo.FORMAT_ARGB32`:
# sfc = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)

# `cairo.Context(target)` creates a new Context to a target surface
#   with all graphics state parameters set to default values.
# The target surface should be constructed with a backend-specific function 
#   such as ImageSurface (or any other cairo backend surface create variant).
ctx = cairo.Context(sfc)


# =============== Draw background =============== #

# `set_source_rgb(red, green, blue)` sets the source pattern within Context to an opaque color.
# This opaque color will then be used for 
#   any subsequent drawing operation until a new source pattern is set.
ctx.set_source_rgb(0.8, 1, 1)

# `rectangle(x, y, width, height)` adds a closed sub-path rectangle 
#   of the given width and height to the current path 
#   at position (x, y) in user-space coordinates.
ctx.rectangle(0, 0, WIDTH, HEIGHT)

# `fill()` fills the current path according to the current fill rule, 
#   (each sub-path is implicitly closed before being filled). 
# After fill(), the current path will be cleared from the Context.
ctx.fill()


# =============== Draw a rectangle =============== #

ctx.set_source_rgb(0.3, 0.4, 0.6)
ctx.rectangle(20, 20, 120, 80)
ctx.fill()

# =============== Write to an image =============== #

output_filename = 'hello_world.png'
# `write_to_png(fobj)` writes the contents of Surface to fobj as a PNG image.
sfc.write_to_png(output_filename)

# Open the output file with default image viewer
os.system(output_filename)