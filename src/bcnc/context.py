from math import *
import sys

class GCodeContext:
    def __init__(self, xy_feedrate, file):
      self.xy_feedrate = xy_feedrate
      self.file = file
      
      self.drawing = False
      self.last = None

      self.preamble = [
        "(G-Code for bCNC software)",
        "G21 (metric ftw)",
        "G90 (absolute mode)",
        "S10000 M3 ( spindle on )",
        "G04 P1 ( 1 second delay to let spindle get up to speed )"
      ]

      self.postscript = [
        "(end of print job)",
        "M5 ( spindle stop )"
        "M02"
      ]

      self.codes = []

    def generate(self):
        codesets = [self.preamble]
        codesets.append(self.codes)
        for codeset in codesets:
            for line in codeset:
              print line
        for line in self.postscript:
            print line

    def start(self):
      self.codes.append("G1 Z-1.0 F200")
      self.drawing = True

    def stop(self):
      self.codes.append("G0 Z0.0 ( spindle up )")
      self.drawing = False

    def go_to_point(self, x, y, stop=False):
      if self.last == (x,y):
        return
      if stop:
        return
      else:
        if self.drawing: 
            self.codes.append("G0 Z0.0") 
            self.drawing = False
        self.codes.append("G0 X%.2f Y%.2f" % (x,y))
      self.last = (x,y)
	
    def draw_to_point(self, x, y, stop=False):
      if self.last == (x,y):
          return
      if stop:
        return
      else:
        if self.drawing == False:
            self.codes.append("G1 Z-1.0 F200")
            self.drawing = True
        self.codes.append("G1 X%0.2f Y%0.2f F%0.2f" % (x,y, self.xy_feedrate))
      self.last = (x,y)
