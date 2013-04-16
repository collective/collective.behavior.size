# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from collective.behavior.size.tests.base import IntegrationTestCase


class TestSetup(IntegrationTestCase):

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_collective_behavior_size_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('collective.behavior.size'))

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(setup.getVersionForProfile(
            'profile-collective.behavior.size:default'), u'0')

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.behavior.size'])
        self.failIf(installer.isProductInstalled('collective.behavior.size'))
