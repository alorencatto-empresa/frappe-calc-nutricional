# Copyright (c) 2025, Augusto Lorencatto and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase

def create_events():

	frappe.set_user("Administrator")
	doc = frappe.get_doc({
		"doctype": "Teste",
		"chave":"Chave de teste",
		"valor":"Valor de teste"
	}).insert()


class TestTeste(FrappeTestCase):
	
	def setUp(self):
		create_events()
	
	# def test_allowed_public(self):
	# 	frappe.set_user("")

	def test_assert(self):
		self.assertTrue(1,1)