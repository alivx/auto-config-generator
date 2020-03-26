#Load jinja Loader function
from libs.jinjaLoader import jinjaLoader

#Run the config template
jinjaLoader("ConfigOutput","config/nginx_conf.json","templates/nginx.conf")