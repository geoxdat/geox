# GeoX

## Installation

For instal this library to your python package library, use command

```bash
pip install geox
```

## Documentation

Here are some examples and feature explanation to use this library

### Initialize API

Initialize GeoX using your `api_key` that can be obtained from Credentials Manager in <https://geoxdat/credential-manager>

```py
app = GeoX(api_key='your-api-key')

# checking the credential by seeing your mail address here
your_email = app.email
```

### Read all of your projects

Read all projects include the detail of each `Project`

```py
app = GeoX(api_key='your-api-key')
projects = app.read_all_projects() # list of Project class
```

### Read specific project

Read a specific project by using by `Project ID`

```py
app = GeoX(api_key='your-api-key')
project = app.read_project('PROJECT-ID') # Project class
```

### Read all project version o specific project

Read all project versions from a `Project`

```py
app = GeoX(api_key='your-api-key')
project = app.read_project('PROJECT-ID') # Project class
project_versions = project.read_all_project_versions() # List of ProjectVerson class
```

### Read specific project version

Read specific project version by project version hash

```py
app = GeoX(api_key='your-api-key')
project = app.read_project('PROJECT-ID') # Project class
project_version = project.read_project_version('project-version-hash') # ProjectVersion class
```

### Read dataset

Read dataset from project version

```py
app = GeoX(api_key='your-api-key')
project = app.read_project('PROJECT-ID') # Project class
project_version = project.read_project_version('project-version-hash') # ProjectVersion 

df_collar = project_version.read_collar_data(save_to_file=False)
df_survey = project_version.read_survey_data(save_to_file=False)
df_alteration = project_version.read_alteration_data(save_to_file=False)
df_assay = project_version.read_assay_data(save_to_file=False)
df_litho = project_version.read_litho_data(save_to_file=False)
df_mineralisation = project_version.read_mineralisation_dat(save_to_file=False)
```

Method parameters:

- `filename` : `str` is the filename if you set the `save_to_file` into `True` (default: `DatasetType`)
- `save_to_file` : `bool` , set it to `True`, you will save the dataset dataframe into file (default: `True`)

### Dataset Type

There are some types of dataset, can be obtained from `DatasetType` object, can be imported using

```py
from geox.entity import DatasetType
```

### Dataset Column

To make it easier for gather information about dataset column, you can use some dataset column objects

```py
from geox.entity import CollarColumn, SurveyColumn, AlterationColumn, AssayColumn, LithoColumn, MineralisationColumn
```

## Copyright

This project is licensed under copyright of GeoX, 2022.

## Our Website

Further informations about dataset, information, integration services, customer support are available in our main website at <https://geoxdat.com>
