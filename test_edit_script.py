import io

from ruamel.yaml import YAML


def edit_file(project, file):
    print(project, file)
    yaml = YAML()
    yaml.indent(mapping=2, sequence=2, offset=0)

    serverless = yaml.load(file.content)
    if 'notificationArn' in serverless['custom']:

        del serverless['custom']['notificationArn']
        serverless['custom']['notificationArns'] = ["arn:aws:sns:us-east-1:915964404932:dh-cf-stack-updates"]
        serverless['service'] = serverless['service'][3:]
        serverless['provider']['stackName'] = 'dh-${opt:stage}-${self:service}'
        string = io.StringIO()
        yaml.dump(serverless, string)
        print(string.getvalue())
