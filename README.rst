========================
collective.behavior.size
========================

collective.behavior.size provides size related behavior, such as weight and three dimensional size, to dexterity content types.

Currently Tested with
---------------------

* Plone-4.3.2 with Python-2.7.x [taito]

Behavior
--------

The behavior can be added through the web or directly through the file system to the dexterity content type xml file like::

  <property name="behaviors">
    ...
    <element value="collective.behavior.size.interfaces.ISize" />
    ...
  </property>
