#Load jinja Loader function
from libs.jinjaLoader import jinjaLoader

#Run the config template
jinjaLoader("ConfigOutput","config/monit.json","templates/monit/monitrc")
print("Please check the config file.")