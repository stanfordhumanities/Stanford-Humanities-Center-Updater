#!/usr/bin/env python
# Copyright 2011, The Board of Regents of Leland Stanford, Jr. University
# All rights reserved. See LICENSE.
# Author: Christine Williams <christine.bennett.williams@gmail.com>
# Description: Configure calendar titles.

import collections

CalendarConfig = collections.namedtuple(
  "CalendarConfig",
  ["calendar_name",  # Human readable calendar name
   "calendar_id",  # Google Calendar ID
    "landing_page_template", # Which template file to use for the landing page
   ])

calendar_ids = [
  CalendarConfig(calendar_name="Stanford Humanities Center Events",
                 calendar_id="stanford.humanities.events%40gmail.com",
                 landing_page_template="events/calendar/index.tmpl"),
  CalendarConfig(calendar_name="Cities Unbound",
                 calendar_id="mllcsrbdpb4caajds3vakb73bc%40group.calendar.google.com",
                 landing_page_template="workshops/calendar/index.tmpl"),
  CalendarConfig(calendar_name="Cognition & Language",
                 calendar_id="qt64bvm60aqgtcnt7dplsq1rds%40group.calendar.google.com",
                 landing_page_template="workshops/calendar/index.tmpl"),
  CalendarConfig(calendar_name="Co-sponsored Events Held at the Humanities Center",
                 calendar_id="otvj0o3d1s8kao8ohg9t4o958s@group.calendar.google.com",
                 landing_page_template="events/calendar/index.tmpl"),
  CalendarConfig(calendar_name="Ethics & Politics, Ancient & Modern",
                 calendar_id="61bjb0uj27vtoq2ueo4fcv609g%40group.calendar.google.com",
                 landing_page_template="workshops/calendar/index.tmpl"),
  CalendarConfig(calendar_name="Equality of Educational Opportunity",
                 calendar_id="tkhs3bg1npl4kmf3682fbpohko%40group.calendar.google.com",
                 landing_page_template="workshops/calendar/index.tmpl"),
  CalendarConfig(calendar_name="French Culture",
                 calendar_id="8ip7um4uemghpos4n2fenqr0dc%40group.calendar.google.com",
                 landing_page_template="workshops/calendar/index.tmpl"),
  CalendarConfig(calendar_name="Graphic Narrative Project",
                 calendar_id="1o8jo65ni7npb02l2kfvi9sibg%40group.calendar.google.com",
                 landing_page_template="workshops/calendar/index.tmpl"),
  CalendarConfig(calendar_name="Interdisciplinary Approaches to Consciousness",
                 calendar_id="bfvev6s9081o7c7vodtp4snbj8@group.calendar.google.com",
                 landing_page_template="workshops/calendar/index.tmpl"),
  CalendarConfig(calendar_name="Modern Middle East",
                 calendar_id="5e85ft4r0lkrmkj1lqic1dsejk@group.calendar.google.com",
                 landing_page_template="workshops/calendar/index.tmpl"),
  CalendarConfig(calendar_name="Interdisciplinary Working Group in Critical Theory",
                 calendar_id="b08oerju95nkffh98pq9k5cauk%40group.calendar.google.com",
                 landing_page_template="workshops/calendar/index.tmpl"),
  CalendarConfig(calendar_name="Language, Information, and Techne",
                 calendar_id="b7j463ob1fi8i39utd5ea4e7tk%40group.calendar.google.com",
                 landing_page_template="workshops/calendar/index.tmpl"),
  CalendarConfig(calendar_name="Recombinations: Art, Medicine, Bioscience",
                 calendar_id="b3jie9nf1i8qcvo730n898nbko%40group.calendar.google.com",
                 landing_page_template="workshops/calendar/index.tmpl"),
  CalendarConfig(calendar_name="Test SHC Calendar",
                 calendar_id="nbeb5t20heagh1j60uq3u2522o@group.calendar.google.com",
                 landing_page_template="events/calendar/index.tmpl"),
  CalendarConfig(calendar_name="Test Workshop Calendar",
                 calendar_id="tn7oa03ign9gpenk8aii7oit44@group.calendar.google.com",
                 landing_page_template="workshops/calendar/index.tmpl"),
  CalendarConfig(calendar_name="Representing Time in Historiography, Ancient and Modern",
                 calendar_id="m805sd1rao2mu7i1j28tv37to8%40group.calendar.google.com",
                 landing_page_template="workshops/calendar/index.tmpl"),
  CalendarConfig(calendar_name="Science and Technology in the Postcolonial World",
                 calendar_id="kodsfm9pa6mfefqtcgbg8ebsq4%40group.calendar.google.com",
                 landing_page_template="workshops/calendar/index.tmpl"),
  CalendarConfig(calendar_name="Spatial Legacies: Urbanism, Movement, and Identity",
                 calendar_id="8lg8kfefafh0o78nf0aaks144k%40group.calendar.google.com",
                 landing_page_template="workshops/calendar/index.tmpl"),
  CalendarConfig(calendar_name="Theoretical Perspectives of the Middle Ages",
                 calendar_id="30kujcrf5h9shk7mlhd2jt6c0s%40group.calendar.google.com",
                 landing_page_template="workshops/calendar/index.tmpl"),
  CalendarConfig(calendar_name="Visualizing Complexity and Uncertainty: Exploring Humanistic "
                               "Approaches to Graphic Representation",
                 calendar_id= "sal6d7mo9rj3l9knn8ot9l69rg%40group.calendar.google.com",
                 landing_page_template="workshops/calendar/index.tmpl")
]
