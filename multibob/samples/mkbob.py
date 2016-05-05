#!/usr/bin/env python
#----------------------------------------------------------------------------
# 05-May-2016 ShaneG
#
# Create a MultiBOB card from a JSON definition. Requires the multibob.svg
# template file.
#----------------------------------------------------------------------------
from sys import argv
from os.path import split, splitext, abspath, join, exists
import xml.etree.ElementTree as ET
import json

# Template file
TEMPLATE = "multibob.svg"

# Namespaces
NS = {
   "dc": "http://purl.org/dc/elements/1.1/",
   "cc": "http://creativecommons.org/ns#",
   "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
   "svg": "http://www.w3.org/2000/svg",
   "sodipodi": "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd",
   "inkscape": "http://www.inkscape.org/namespaces/inkscape",
  }

# Sample data
SAMPLE = {
  "title": "This is a sample",
  "jumpers": [ 2, 3, 4 ],
  "components": {
    "comp1": ( "U1", "MCP1702 (3.3V)" ),
    "comp5": ( "R1", "10K" ),
    "comp6": ( "R2", "5K" ),
    },
  "pins": [
    "Vin",
    "Gnd",
    "Vout"
    ]
  }

#----------------------------------------------------------------------------
# Template processing
#----------------------------------------------------------------------------

def findJumper(root, name):
  """ Find a jumper. Returns the parent and the jumper
  """
  global NS
  return (
    root.find(".//svg:ellipse[@id='%s']/.." % name, NS),
    root.find(".//svg:ellipse[@id='%s']" % name, NS)
    )

def findComponent(root, name):
  """ Find a component. Returns the parent, the component and the text block
  """
  global NS
  return (
    root.find(".//svg:g[@id='%s']/.." % name, NS),
    root.find(".//svg:g[@id='%s']" % name, NS),
    root.find(".//svg:g[@id='%s']//svg:tspan" % name, NS),
    )

def findDescriptions(root):
  """ Find all the descriptions
  """
  global NS
  results = list()
  for i in range(6):
    name = "desc%d" % (i + 1)
    results.append((
      root.find(".//svg:g[@id='%s']/.." % name, NS),
      root.find(".//svg:g[@id='%s']" % name, NS),
      root.find(".//svg:g[@id='%s']//svg:text[1]/svg:tspan" % name, NS),
      root.find(".//svg:g[@id='%s']//svg:text[2]/svg:tspan" % name, NS),
      ))
  return results

def findPins(root):
  """ Find all the pins
  """
  global NS
  results = list()
  for i in range(3):
    name = "pin%d" % (i + 1)
    results.append(root.find(".//svg:text[@id='%s']/svg:tspan" % name, NS))
  return results

def process(data):
  """ Create an XML tree from the template with the data given
  """
  global TEMPLATE, NS
  tree = ET.parse(TEMPLATE)
  root = tree.getroot()
  # Update the title
  title = root.find(".//svg:text[@id='title']/svg:tspan", NS)
  title.text = str(data['title'])
  # Update jumpers
  for i in range(5):
    parent, jump = findJumper(root, "jump%d" % (i + 1))
    if not (i + 1) in data['jumpers']:
      parent.remove(jump)
  # Update components
  for i in range(7):
    name = "comp%d" % (i + 1)
    parent, comp, text  = findComponent(root, name)
    if not name in data['components'].keys():
      parent.remove(comp)
    else:
      text.text = data['components'][name][0]
  # Update descriptions
  values = tuple([ data['components'][x] for x in sorted(data['components'].keys()) ])
  fields = findDescriptions(root)
  for name, content in values:
    parent, desc, nameField, contentField = fields[0]
    nameField.text = str(name)
    contentField.text = str(content)
    del fields[0]
  for parent, desc, nameField, contentField in fields:
    parent.remove(desc)
  # Update pins
  pins = findPins(root)
  for i in range(3):
    pins[i].text = str(data['pins'][i])
  # All done
  return tree

#----------------------------------------------------------------------------
# Main program
#----------------------------------------------------------------------------

if __name__ == "__main__":
  # Check the arguments
  if len(argv) <> 2:
    print "Usage:"
    print "        %s filename[.json]" % split(__file__)[1]
    exit(1)
  # Determine the full path to the template
  TEMPLATE = join(split(abspath(__file__))[0], TEMPLATE)
  # Get the name of the input file
  name, ext = splitext(argv[1])
  if ext == "":
    ext = ".json"
  # Load the data and process it
  filename = name + ext
  if not exists(filename):
    print "Error: File '%s' was not found" % filename
    exit(1)
  try:
    data = json.load(open(filename, "r"))
    result = process(data)
    # Write out the result
    result.write(name + ".svg")
  except Exception, ex:
    print "Error: Unable to process '%s' - %s" % (filename, str(ex))
