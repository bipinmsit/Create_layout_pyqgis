import sys
from qgis.core import *
from PyQt4.QtCore import *
from PyQt4.QtXml import *
from qgis.core import *
from qgis.gui import *
import argparse
import logging
import json

gui_flag = True
app = QgsApplication(sys.argv, gui_flag)

# Make sure QGIS_PREFIX_PATH is set in your env if needed!
app.initQgis()

# Probably you want to tweak this
project_path = 'single_pdf.qgs'
template_path = 'test.qpt'

def create_layout(input_raster, input_json):

    canvas = QgsMapCanvas()

    # Load our project
    QgsProject.instance().read(QFileInfo(project_path))

    # Load layers here if they are not already in the project

    fileInfo = QFileInfo(input_raster)
    path = fileInfo.filePath()
    baseName = fileInfo.baseName()
    layer = QgsRasterLayer(path, baseName)
    QgsMapLayerRegistry.instance().addMapLayer(layer)

    if layer.isValid() is True:
        print "Layer was loaded successfully!"
    else:
        print "Unable to read basename and file path"

    # Bridge used in standalone script
    bridge = QgsLayerTreeMapCanvasBridge(
        QgsProject.instance().layerTreeRoot(), canvas)
    bridge.setCanvasLayers()

    template_file = file(template_path)
    template_content = template_file.read()
    template_file.close()
    document = QDomDocument()
    document.setContent(template_content)
    composition = QgsComposition(canvas.mapSettings())

    with open(input_json, "r") as config_file:
        input_dict = json.load(config_file)

    composition.loadFromTemplate(document, input_dict)

    # You must set the id in the template
    map_item = composition.getComposerItemById('Map Frame')
    map_item.setMapCanvas(canvas)
    map_item.zoomToExtent(canvas.extent())

    # You must set the id in the template
    legend_item = composition.getComposerItemById('Layout Frame')
    #legend_item.updateLegend()
    composition.refreshItems()
    composition.exportAsPDF('export.pdf')
    QgsProject.instance().clear()
    QgsApplication.exitQgis()

parser = argparse.ArgumentParser(description="Add Input Parameters for Creating the Layout")
parser.add_argument("-ir", "--Input_Raster", required = True, help = "Raster File Path")
parser.add_argument("-ij", "--Input_JSON", required = True, help = "Input JSON File")
args = parser.parse_args()

if __name__ == "__main__":
    create_layout(args.Input_Raster, args.Input_JSON)
