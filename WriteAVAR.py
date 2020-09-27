#MenuTitle: Write AVAR table
# -*- coding: utf-8 -*-
import vanilla

__doc__="""
Writes an AVAR table based on current weight distribution
"""

font = Glyphs.font

axisMinimum = font.instances[0].weightValue # lightest stem weight
axisRange = font.instances[-1].weightValue - axisMinimum # boldest stem weight

# create a dictionary which indexes all instances by weight
instancelist = sorted({font.instances[i].weightValue for i in range(len(font.instances))})

# create a dictionary which stores the AVAR table
avartable = {"wght": {int(axisRange/(len(instancelist)-1)*l+axisMinimum):instancelist[l] for l in range(len(instancelist))}}

# write AVAR table to custom parameters
font.customParameters["Axis Mappings"] = avartable