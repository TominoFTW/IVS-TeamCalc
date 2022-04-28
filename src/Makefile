.PHONY: all pack clean test doc run profile

all: 
	echo "Project is using Python (no build needed)"

clean:
	for line in `cat ../.gitignore | grep -v ^# | sed 's|/||' | sed 's/\r//'`; do rm -rf `find . -name $$line 2>/dev/null`; done

test:
	/usr/bin/env python3 -m tests

doc: Doxyfile
	doxygen

run:
	/usr/bin/env python3 calc.py

profile:
	echo "Using Python, no need to build"
