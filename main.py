from geox import GeoX


geox = GeoX(api_key='iI5NXd5VvrblQ4RBpssF3PReuOQMLP9U')
project = geox.read_project('TST0001')
print(geox._timestamp)