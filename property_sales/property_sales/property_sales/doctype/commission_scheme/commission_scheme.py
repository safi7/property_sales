# -*- coding: utf-8 -*-
# Copyright (c) 2019, Tektician Sdn Bhd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CommissionScheme(Document):
	pass


@frappe.whitelist()
def get_names(parent):
	j=""
	for i in frappe.db.sql("""select disbursement_name from `tabDisbursement Schedule` where 
	 parent=%s""",parent,as_dict=1):

		j = j+i.disbursement_name+("\n")

	return j

@frappe.whitelist()
def get_description(parent, name1):
	d= frappe.db.sql("""select disbursement_description as descs from `tabDisbursement Schedule` where 
	 parent=%s and disbursement_name=%s""",(parent,name1),as_dict=1)

		

	return d

