#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2011, The Board of Regents of Leland Stanford, Jr. University
# All rights reserved. See LICENSE.
# Author: Christine Williams <christine.bennett.williams@gmail.com>

import unittest

import re

def FixTemplates(source, fragments={}, title=''):
  fixed = source.replace('$(', r'\$(')
  fixed = re.sub(r'<title>[^|]+\|', '<title>' + title + '|', fixed)
  def GetFragment(matches):
    return fragments[matches.group(1)]
  fixed = re.sub(r'<!--code:(\w+)-->', GetFragment, fixed)
  return fixed


class FixerTest(unittest.TestCase):
  def testFixDollarSign(self):
    self.assertEquals(r'stuff \$(foo)', FixTemplates('stuff $(foo)'))
    
  def testReplaceCodeComment(self):
    self.assertEquals('stuff {{code}} stuff',
                      FixTemplates('stuff <!--code:foo--> stuff',
                                   fragments={'foo': '{{code}}'}))
                      
  def testReplace2CodeComments(self):
    self.assertEquals('stuff {{code}} stuff {{morecode}}',
                      FixTemplates('stuff <!--code:foo--> stuff <!--code:bar-->',
                                   fragments={'foo': '{{code}}', 'bar': '{{morecode}}'}))
                                   
  def testReplaceTitle(self):
    self.assertEquals('stuff <title>{{code}}| More stuff</title>',
                      FixTemplates('stuff <title>Events | More stuff</title>',
                                   title='{{code}}'))
  
  
if __name__ == '__main__':
  unittest.main()