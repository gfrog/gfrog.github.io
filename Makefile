PY?=python3
PELICAN?=pelican
PELICANOPTS=
SEDPROGRAM=gsed

PROXY_ENV=proxychains4

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=/tmp/pelican-output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

GITHUB_PAGES_BRANCH=master


DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80    '
	@echo '   make devserver [PORT=8000]          serve and regenerate together      '
	@echo '   make ssh_upload                     upload the web site via SSH        '
	@echo '   make rsync_upload                   upload the web site via rsync+ssh  '
	@echo '   make github                         upload the web site via gh-pages   '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

html:
	$(PROXY_ENV) $(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
	grep '<table>' $(OUTPUTDIR)  -rl  --include '*.html' \ | xargs $(SEDPROGRAM) -i 's/<table>/<table class="table table-condensed table-bordered table-hover">/'

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate:
	$(PROXY_ENV) $(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT)
else
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
endif

serve-global:
ifdef SERVER
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT) -b $(SERVER)
else
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT) -b 0.0.0.0
endif


devserver:
ifdef PORT
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT)
else
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
endif

publish:
	$(PROXY_ENV) $(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)
	grep '<table>' $(OUTPUTDIR)  -rl  --include '*.html' \ | xargs $(SEDPROGRAM) -i 's/<table>/<table class="table table-condensed table-bordered table-hover">/'

github: publish
	ghp-import -pf -m "Generate Pelican site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	#git push origin $(GITHUB_PAGES_BRANCH)


.PHONY: html help clean regenerate serve serve-global devserver stopserver publish github