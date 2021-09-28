TOPLEVEL_LANG ?= vhdl
SIM ?= ghdl
VHDL_SOURCES = test.vhdl
TOPLEVEL := test
MODULE := test

include $(shell cocotb-config --makefiles)/Makefile.sim
