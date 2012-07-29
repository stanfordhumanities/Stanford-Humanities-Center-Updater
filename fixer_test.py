#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2011, The Board of Regents of Leland Stanford, Jr. University
# All rights reserved. See LICENSE.
# Author: Christine Williams <christine.bennett.williams@gmail.com>

import unittest

import re

def FixTemplates(source, fragments):
  fixed = source.replace('$(', r'\$(')
  def GetFragment(matches):
    return fragments[matches.group(1)]
  fixed = re.sub(r'<!--code:(\w+)-->', GetFragment, fixed)
  return fixed


class FixerTest(unittest.TestCase):
  def testFixDollarSign(self):
    self.assertEquals(r'stuff \$(foo)', FixTemplates('stuff $(foo)', None))
    
  def testReplaceCodeComment(self):
    self.assertEquals('stuff {{code}} stuff',
                      FixTemplates('stuff <!--code:foo--> stuff', {'foo': '{{code}}'}))
                      
  def testReplace2CodeComments(self):
    self.assertEquals('stuff {{code}} stuff {{morecode}}',
                      FixTemplates('stuff <!--code:foo--> stuff <!--code:bar-->',
                                   {'foo': '{{code}}', 'bar': '{{morecode}}'}))
  
  
if __name__ == '__main__':
  unittest.main()