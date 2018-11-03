book:
	@clear && rm -fr .build && sphinx-build -j10 -b html . .build/

help:
	@sphinx-build -M help help help

clean:
	-rm -fr .build/
