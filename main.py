from geox import GeoX


geox = GeoX(api_key='POmg5QSkDeNYTfxSeRqsl4sk9OWmHTON')
project = geox.read_project('NANO000')
# # project_versions = project.read_all_project_versions()
project_version = project.read_project_version('kosHBHi6es2AzLIzkY4CNnksYNGC7SHd')
df_collar = project_version.read_collar_data(save_to_file=False)
df_survey = project_version.read_survey_data(save_to_file=False)
df_alteration = project_version.read_alteration_data(save_to_file=False)
df_assay = project_version.read_assay_data(save_to_file=False)
df_litho = project_version.read_litho_data(save_to_file=False)
df_mineralisation = project_version.read_mineralisation_data(save_to_file=False)
print(geox._timestamp)