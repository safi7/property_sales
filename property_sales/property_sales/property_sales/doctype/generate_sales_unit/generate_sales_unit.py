# -*- coding: utf-8 -*-
# Copyright (c) 2019, Tektician Sdn Bhd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class GenerateSalesUnit(Document):
	pass

@frappe.whitelist()
def get_bill_of_material(parent):
	d = frappe.db.get_list("Bill of Material Items", filters={"parent": parent}, fields = ["building_name"])
	return d

@frappe.whitelist()
def checkduplicate(project,bill_of_material,building_name,creation):
       return frappe.db.sql("""Select * from  `tabGenerate Sales Unit`
		where project_name=%s  and phase_name=%s and building_name=%s and creation!=%s""", (project,bill_of_material,building_name,creation), as_dict=True)
		
@frappe.whitelist()
def checkduplicatewithoutdate(project,bill_of_material,building_name):
	return frappe.db.sql("""Select * from  `tabGenerate Sales Unit`
	where project_name=%s  and phase_name=%s and building_name=%s""", (project,bill_of_material,building_name), as_dict=True)

@frappe.whitelist()
def get_bill_of_material_count(parent, building_name):
	d = frappe.db.sql("""Select * from  `tabBill of Material Building Count`
	where parent=%s and building_name=%s""", (parent, building_name), as_dict=True)
	return d
	
@frappe.whitelist()
def insert_serial_no(serial_no,item_code,lot_types):
	Event_doc=frappe.new_doc("Serial No")
	Event_doc.serial_no=serial_no;
	Event_doc.item_code=item_code;
	Event_doc.lot_types=lot_types;
	Event_doc.save()

@frappe.whitelist()
def get_item(name):
	d = frappe.db.sql("""Select * from  `tabItem Variant Attribute`
	where parent=%s """, (name), as_dict=True)
	return d
	
@frappe.whitelist()
def serial_delete(serialno):
		return frappe.db.sql("""Delete from `tabSerial No` where name=%s """,
			(serialno), as_dict=True)