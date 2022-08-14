from geox import GeoX


geox = GeoX(api_key='iI5NXd5VvrblQ4RBpssF3PReuOQMLP9U')
geox.read_all_projects()
print(geox._timestamp)