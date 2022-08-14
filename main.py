from geox import GeoX


geox = GeoX(api_key='iI5NXd5VvrblQ4RBpssF3PReuOQMLP9U')
project = geox.read_project('TST000')
project_versions = project.read_all_project_versions()
print(geox._timestamp)