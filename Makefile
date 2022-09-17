RM    := rm -rf
MKDIR := mkdir -p
PYTHON := python

all: cpplib pypackage

cpplib:
	@  ($(MKDIR) build > /dev/null)
	@  (cd build > /dev/null 2>&1 && cmake ..)
	@ $(MAKE) -C build

pypackage:
	@ ${PYTHON} -m build

clean:
	@  ($(MKDIR) build > /dev/null)
	@  (cd build > /dev/null 2>&1 && cmake .. > /dev/null 2>&1)
	@- $(MAKE) --silent -C build clean || true
	@- $(RM) ./build/CMake*
	@- $(RM) ./build/cmake.*
	@- $(RM) ./build/Makefile
	@- $(RM) ./build/*.cmake
	@- $(RM) ./build/*.txt
	@- ${RM} ./dist/

