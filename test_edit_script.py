import io

from ruamel.yaml import YAML


def edit_file(project, file, save_cb):

    yaml = YAML()
    yaml.indent(mapping=2, sequence=2, offset=0)

    serverless = yaml.load(file.content)
    print('serverless loaded')

    serverless['custom']['notificationArns'] = ["${ssm:/dh/${opt:stage}/infra/cf-stack-updates}"]
    string = io.StringIO()
    yaml.dump(serverless, string)
    print(string.getvalue())
    file.content = string.getvalue()
    save_cb()

