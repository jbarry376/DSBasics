# ---------------------------------
# Demo using xml.dom.minidom to parse xml data 
# Parsing elements and adding a new element 
# ---------------------------------
# using sample data : milesDavis.xml 

from xml.dom.minidom import parse

def main():
  # use the parse() function to load and parse an XML file
  doc = parse("data/milesDavis.xml")
  
  # print out the document node and the name of the first child tag
  print (doc.nodeName)
  print (doc.firstChild.tagName)

  print("-----------------------------")
  # get a list of XML tags from the document and print each one
  tracks = doc.getElementsByTagName("track")
  print("List of songs on the original Album: ")
  print ("%d Tracks:" % tracks.length)
  for track in tracks:
    print (track.getAttribute("song"))
  
  print("-----------------------------")
  # create a new XML tag and add it into the document
  newTrack = doc.createElement("track")
  newTrack.setAttribute("song", "Blue in Green (Studio Sequence)")
  doc.firstChild.appendChild(newTrack)

  tracks = doc.getElementsByTagName("track")
  print("List of songs on updated Album: ")
  print ("%d Tracks:" % tracks.length)
  for track in tracks:
    print (track.getAttribute("song"))
        
if __name__ == "__main__":
  main()