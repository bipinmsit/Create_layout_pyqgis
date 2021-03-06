:: http://gis.stackexchange.com/a/144909

REM Change OSGeo4W_ROOT to point to your install of QGIS.

SET OSGEO4W_ROOT=C:\Program Files\QGIS 2.18
SET QGISNAME=qgis
SET QGIS=%OSGEO4W_ROOT%\apps\%QGISNAME%
set QGIS_PREFIX_PATH=%QGIS%

CALL "%OSGEO4W_ROOT%\bin\o4w_env.bat"

: Python Setup
set PATH=%OSGEO4W_ROOT%\\apps\\qgis\\bin;%PATH%
SET PYTHONHOME=%OSGEO4W_ROOT%\\apps\Python27
set PYTHONPATH=%OSGEO4W_ROOT%\\apps\\qgis\\python

ECHO OSGeo path is: %OSGEO4W_ROOT%
ECHO Getting QGIS libs from: %QGIS%
ECHO Python loaded from: %PYTHONHOME%

C:\Python27\python\python.exe demo.py -ir "C:\Users\user\Downloads\INFOSYS-PHASE-1-SEZ-Dev-Development-Area-mosaic-utm-clipped.tif" -ij "C:\Users\user\Desktop\GitHub\qgis-standalone-map-export\json_for_layout.json"