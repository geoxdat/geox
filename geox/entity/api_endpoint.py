from geox.config import SERVER_HOST


class APIEndpoint:
    """Server endpoint, pointed to server host
    """
    __API_V1_EXTERNAL = SERVER_HOST + '/v1/geox'

    GET_INITIAL_AUTH = __API_V1_EXTERNAL + '/init'
    GET_USER_PROJECTS = __API_V1_EXTERNAL + '/project/all'
    GET_PROJECT = __API_V1_EXTERNAL + '/project'

    GET_PROJECT_VERSIONS = __API_V1_EXTERNAL + '/project/version/all'
    GET_PROJECT_VERSION = __API_V1_EXTERNAL + '/project/version'

    GET_COLLAR_DATA = __API_V1_EXTERNAL + '/dataset/collar'
    GET_SURVEY_DATA = __API_V1_EXTERNAL + '/dataset/survey'
    GET_ALTERATION_DATA = __API_V1_EXTERNAL + '/dataset/alteration'
    GET_ASSAY_DATA = __API_V1_EXTERNAL + '/dataset/assay'
    GET_LITHO_DATA = __API_V1_EXTERNAL + '/dataset/litho'
    GET_MINERALISATION_DATA = __API_V1_EXTERNAL + '/dataset/mineralisation'