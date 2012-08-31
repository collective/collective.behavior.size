========================
collective.behavior.size
========================

collective.behavior.size provides size related behavior, such as weight and three dimensional size, to dexterity content types.

Currently Tested with
---------------------

* Plone-4.2.1 [taito]

Behavior
--------

The behavior can be added through the web or directly through the file system to the dexterity content type xml file like::

  <property name="behaviors">
    ...
    <element value="collective.behavior.size.interfaces.ISize" />
    ...
  </property>

Farther Documentation URL
-------------------------

`http://packages.python.org/collective.behavior.size/
<http://packages.python.org/collective.behavior.size/>`_

Repository URL
--------------

`https://github.com/collective/collective.behavior.size/
<https://github.com/collective/collective.behavior.size/>`_
