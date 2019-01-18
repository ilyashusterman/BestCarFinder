################################################################################
# Makefile for BestCarFinder
################################################################################

# Prefer bash shell
export SHELL=/bin/bash

## Define repositories dependencies paths

## Make sure of current python path
#export PYTHONPATH=backend:$(pwd):$(CYBERCOMB_PATH):$(GRADER_PATH):~/dev

self := $(abspath $(lastword $(MAKEFILE_LIST)))
parent := $(dir $(self))

ifneq (,$(VERBOSE))
    override VERBOSE:=
else
    override VERBOSE:=@
endif

.PHONY: test
test:
	$(VERBOSE) nosetests