from fabric.api import task, local, settings
import sys
import os
import time

browser = "firefox"

if sys.platform == 'darwin':
    browser = "open"

@task
def all():
    html()
    pdf()
    epub()

@task
def clean():
    pass
    
@task    
def view(kind='html'):
    if kind == 'html':
        """view the documentation in a browser"""
        local("{browser} docs/build/html/index.html".format(browser=browser))
    else:
        local("open docs/build/epub/cloudaqua.epub")
        
def theme(name='bootstrap'):
    os.environ['SPHINX_THEME'] = name
    if os.environ['SPHINX_THEME'] == 'bootstrap':
        local('cp docs/source/_templates/layout_bootstrap.html docs/source/_templates/layout.html')
    else:
        local('cp docs/source/_templates/layout_simple.html docs/source/_templates/layout.html')
    
@task
def html(theme_name='bootstrap'):
    # disable Flask RSTPAGES due to sphins incompatibility
    os.environ['RSTPAGES'] = 'FALSE'
    theme(theme_name)
    # api()
    # man()
    """build the doc locally and view"""
    clean()
    local("cd docs; make html")

@task
def pdf():
    theme('simple')
    with settings(warn_only=True):
        local("cd docs; echo 'r' | make latexpdf")
    local("cp docs/build/latex/myCloudmesh.pdf docs/build/html/myCloudmesh.pdf")
        
@task
def epub():
    theme('simple')
    with settings(warn_only=True):
        local("cd docs; make epub")
    local("cp docs/build/epub/myCloudmesh.epub docs/build/html/myCloudmesh.epub")
    
@task
def fast(theme_name='bootstrap'):
    theme(theme_name)
    local("cd docs; make html")

@task
def simple():
    local("cd docs; make html")
            
@task
def publish():
    """deploy the documentation on gh-pages"""
    #html()
    local('cd docs/build/html && git add .  && git commit -m "site generated" && git push origin gh-pages')
    local('git commit -a -m "build site"')
    local("git push origin master")


@task
def man():
    """deploy the documentation on gh-pages"""
    #TODO: match on "Commands"
    local("cm man | grep -A10000 \"Commands\"  | sed \$d  > docs/source/man/man.rst")

@task
def api():
    for modulename in ["cloudmesh", "cloudmesh_common", "cloudmesh_install", "cmd3local", "cloudmesh_web"]:
        print 70 * "="
        print "Building API Doc:", modulename 
        print 70 * "="        
        local("sphinx-apidoc -f -o docs/source/api/{0} {0}".format(modulename))



