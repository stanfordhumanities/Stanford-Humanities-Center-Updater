#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2011, The Board of Regents of Leland Stanford, Jr. University
# All rights reserved. See LICENSE.
# Author: Christine Williams <christine.bennett.williams@gmail.com>

import unittest

import fixer



class FixerTest(unittest.TestCase):
  def testFixDollarSign(self):
    self.assertEquals(r'stuff \$(foo)', fixer.FixTemplate('stuff $(foo)'))
    
  def testReplaceCodeComment(self):
    self.assertEquals('stuff {{code}} stuff',
                      fixer.FixTemplate('stuff <!--code:foo--> stuff',
                                        fragments={'foo': '{{code}}'}))
                      
  def testReplace2CodeComments(self):
    self.assertEquals('stuff {{code}} stuff {{morecode}}',
                      fixer.FixTemplate('stuff <!--code:foo--> stuff <!--code:bar-->',
                                        fragments={'foo': '{{code}}', 
                                                   'bar': '{{morecode}}'}))
                                   
  def testReplaceTitle(self):
    self.assertEquals('stuff <title>{{code}}| More stuff</title>',
                      fixer.FixTemplate('stuff <title>Events | More stuff</title>',
                                        title='{{code}}'))
                                   
  def testUnfixed(self):
    self.assertTrue(fixer.NeedsConversion('stuff $(badness)'))
    
  def testFixed(self):
    self.assertFalse(fixer.NeedsConversion(r'stuff \$(badness)'))
  
  
if __name__ == '__main__':
  unittest.main()