#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# @package ivscalc
# Main ivscalc module.

##
# @brief Main ivscalc module.
import re
import sys
from ivscalc.calc import main
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())