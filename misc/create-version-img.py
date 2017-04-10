#!/usr/bin/env python

import gd, math


i = gd.image((244,144))
t = i.colorAllocate((255, 255, 255))
i.filledRectangle((0,0), (244, 144), t)
i.colorTransparent(t)
black = i.colorAllocate((0,0,0))
i.string_ttf('./charrington.posh.ttf', 100, 0, (20,110), "1.1.0", black)
red = i.colorAllocate((153,0,0))
i.string_ttf('./old_stamper.ttf', 40, 0.12 * math.pi, (20, 130), "Alpha 1", red)
i.writePng('1.1.0-alpha-1.png')

i = gd.image((244,144))
t = i.colorAllocate((255, 255, 255))
i.filledRectangle((0,0), (244, 144), t)
i.colorTransparent(t)
black = i.colorAllocate((0,0,0))
i.string_ttf('./charrington.posh.ttf', 100, 0, (20,110), "1.1.0", black)
red = i.colorAllocate((153,0,0))
i.string_ttf('./old_stamper.ttf', 38, -0.1 * math.pi, (8, 60), "Alpha 2", red)
i.writePng('1.1.0-alpha-2.png')

i = gd.image((244,144))
t = i.colorAllocate((255, 255, 255))
i.filledRectangle((0,0), (244, 144), t)
i.colorTransparent(t)
black = i.colorAllocate((0,0,0))
i.string_ttf('./charrington.posh.ttf', 100, 0, (4,110), "1.0.0", black)
green = i.colorAllocate((0,102,0))
i.string_ttf('./old_stamper.ttf', 46, 0.12 * math.pi, (20, 130), "Beta 1", green)
i.writePng('1.0.0-beta-1.png')

i = gd.image((244,144))
t = i.colorAllocate((255, 255, 255))
i.filledRectangle((0,0), (244, 144), t)
i.colorTransparent(t)
black = i.colorAllocate((0,0,0))
i.string_ttf('./charrington.posh.ttf', 100, 0, (4,110), "1.0.0", black)
green = i.colorAllocate((0,102,0))
i.string_ttf('./old_stamper.ttf', 44, -0.1 * math.pi, (8, 60), "Beta 2", green)
i.writePng('1.0.0-beta-2.png')
