# Following https://trac.edgewall.org/wiki/PySqlite#BuildingonWindows

# Using https://github.com/stuarteberg/conda-multisrc-example/ to download both pysqlite and sqlite-amalgamation

for /f %%i in ('conda info --root') do set CONDA_PYTHON=%%i\python
%CONDA_PYTHON% %RECIPE_DIR%\download-extra-sources.py
if errorlevel 1 exit 1

mkdir internal
echo %cd%
xcopy /s ..\..\..\work\sqlite-amalgamation-3180000\sqlite3.c internal\
xcopy /s ..\..\..\work\sqlite-amalgamation-3180000\sqlite3.h internal\
xcopy /s ..\..\..\work\sqlite-amalgamation-3180000\shell.c internal\
xcopy /s ..\..\..\work\sqlite-amalgamation-3180000\sqlite3ext.h internal\
if errorlevel 1 exit 1

cd internal
cl -c sqlite3.c
if errorlevel 1 exit 1
lib sqlite3.obj -out:sqlite3.lib
if errorlevel 1 exit 1

cd ..
"%PYTHON%" setup.py install
if errorlevel 1 exit 1