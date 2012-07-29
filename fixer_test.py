#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2011, The Board of Regents of Leland Stanford, Jr. University
# All rights reserved. See LICENSE.
# Author: Christine Williams <christine.bennett.williams@gmail.com>

import unittest

import re

def FixTemplate(source, fragments={}, title=''):
  """Fixes up RapidWeaver published html files into valid Cheetah templates.
  
  The algorithm is:
  1. Replace $( with \$(, because this innocent-looking jQuery syntax confuses Cheetah.
  2. Replace <!--code:fragment-name--> with fragments[fragment-name].
  3. Replace everything between <title> and | with title.
  
  Args:
    source: The original HTML published by RapidWeaver.
    fragments: A dictionary of fragment-name to fragment content. Any comments in source
      that match <!--code:fragment-name--> are replaced by looking up fragment-name in
      this dictionary and replacing the whole comment with the value.
    title: Template fragment to insert between <title> and |.
    
  Returns:
    A valid Cheetah template.
  """
  fixed = source.replace('$(', r'\$(')
  fixed = re.sub(r'<title>[^|]+\|', '<title>' + title + '|', fixed)
  def GetFragment(matches):
    return fragments[matches.group(1)]
  fixed = re.sub(r'<!--code:(\w+)-->', GetFragment, fixed)
  return fixed
  
  
def NeedsConversion(source):
  """Check source to see if it was just publish by RapidWeaver and not yet fixed."""
  return '<!--code' in source or re.search(r'[^\\]\$\(', source)


class FixerTest(unittest.TestCase):
  def testFixDollarSign(self):
    self.assertEquals(r'stuff \$(foo)', FixTemplate('stuff $(foo)'))
    
  def testReplaceCodeComment(self):
    self.assertEquals('stuff {{code}} stuff',
                      FixTemplate('stuff <!--code:foo--> stuff',
                                  fragments={'foo': '{{code}}'}))
                      
  def testReplace2CodeComments(self):
    self.assertEquals('stuff {{code}} stuff {{morecode}}',
                      FixTemplate('stuff <!--code:foo--> stuff <!--code:bar-->',
                                  fragments={'foo': '{{code}}', 'bar': '{{morecode}}'}))
                                   
  def testReplaceTitle(self):
    self.assertEquals('stuff <title>{{code}}| More stuff</title>',
                      FixTemplate('stuff <title>Events | More stuff</title>',
                                 title='{{code}}'))
                                   
  def testUnfixed(self):
    self.assertTrue(NeedsConversion('stuff $(badness)'))
    
  def testFixed(self):
    self.assertFalse(NeedsConversion(r'stuff \$(badness)'))
  
  
if __name__ == '__main__':
  unittest.main()