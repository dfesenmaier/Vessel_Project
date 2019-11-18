from qgis.core import *
from processing.tools.vector import VectorWriter
 
Input_Table = 'ais_sample_new.csv'
lon_field = 'y' 
lat_field = 'x' 
crs = 4326 
Output_Layer = 'ais_sample_new.shp' 
 
spatRef = QgsCoordinateReferenceSystem(crs, QgsCoordinateReferenceSystem.EpsgCrsId)
 
inp_tab = QgsVectorLayer(Input_Table, 'Input_Table', 'ogr')
prov = inp_tab.dataProvider()
fields = inp_tab.pendingFields()
outLayer = QgsVectorFileWriter(Output_Layer, None, fields, QGis.WKBPoint, spatRef)
 
pt = QgsPoint()
outFeature = QgsFeature()
 
for feat in inp_tab.getFeatures():
    attrs = feat.attributes()
    pt.setX(float(feat[lon_field]))
    pt.setY(float(feat[lat_field]))
    outFeature.setAttributes(attrs)
    outFeature.setGeometry(QgsGeometry.fromPoint(pt))
    outLayer.addFeature(outFeature)
del outLayer