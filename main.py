from geox import GeoX


geox = GeoX(api_key='iI5NXd5VvrblQ4RBpssF3PReuOQMLP9Uj')
geox.read_all_projects()
print(geox._timestamp)