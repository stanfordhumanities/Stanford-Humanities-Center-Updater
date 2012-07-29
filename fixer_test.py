#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2011, The Board of Regents of Leland Stanford, Jr. University
# All rights reserved. See LICENSE.
# Author: Christine Williams <christine.bennett.williams@gmail.com>

import unittest

def FixTemplates(source):
  return source.replace('$(', r'\$(')


class FixerTest(unittest.TestCase):
  def testFixDollarSign(self):
    self.assertEquals(r'stuff \$(foo)', FixTemplates('stuff $(foo)'))
  
  
if __name__ == '__main__':
  unittest.main()