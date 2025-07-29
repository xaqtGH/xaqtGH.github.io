echo off
cls

del     out.json
python  datavisualize.py
Rscript graph.r

echo Success!