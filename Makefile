all:
	cd docs; make -f Makefile html

gh-pages:
	cd docs/build/html && git add .  && git commit -m "site generated" && git push origin gh-pages	
	git commit -a -m "build site"
	git push origin master	

view:
	open docs/build/html/index.html
