import io
import toml

dict = [{'name': 'dh_common_gitlab', 'url': 'https://gitlab.com/api/v4/projects/18129642/packages/pypi/simple', 'secondary': True},
 {'name': 'dh_cqrs_gitlab', 'url': 'https://gitlab.com/api/v4/projects/19708305/packages/pypi/simple', 'secondary': True},
 {'name': 'dh_api_doc_generator_gitlab', 'url': 'https://gitlab.com/api/v4/projects/21477008/packages/pypi/simple', 'secondary': True}]


def edit_file(project, file, save_cb):
    print('bla')
    pyproject = toml.loads(file.content)
    pyproject['tool']['poetry']['source'] = dict

    file.content = toml.dumps(pyproject)
    save_cb()
