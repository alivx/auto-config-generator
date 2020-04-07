def jinjaLoader(outputDir, configFile, templateFile):
    """
    jinjaLoader generate config file based on template and key,value config json file

    Args:
        outputDir (str): generated file output dir
        configFile (str): config file that contain the key value config
        templateFile (str): origin template config file
    """
    import jinja2
    import json
    import os

    # Nginx config template file
    output_dir = "ConfigOutput"

    # Load json config file
    config_File = open(configFile)
    config_parameters = json.load(config_File)
    serviceName = "{0}.conf".format(config_parameters[0]['name'])

    loader = jinja2.Environment(loader=jinja2.FileSystemLoader(
        searchpath="."), trim_blocks=True, lstrip_blocks=True)
    tempFile = loader.get_template(templateFile)

    # we will make sure that the output directory exists
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # now create the templates
    print("Create templates...")
    for config in config_parameters:
        result = tempFile.render(config)
        f = open(os.path.join(output_dir, serviceName), "w")
        f.write(result)
        f.close()
        print("Output file: {0}".format(os.path.join(output_dir, serviceName)))
