# -*- coding: utf-8 -*-
# Copyright (c) 2019, Tektician Sdn Bhd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class PropertySales(Document):
	pass

@frappe.whitelist()
def get_bill_of_material(parent):
	d = frappe.db.get_list("Bill of Material Items", filters={"parent": parent}, fields = ["building_name"])
	return d

@frappe.whitelist()
def checkduplicate(project,bill_of_material,building_name,creation):
       return frappe.db.sql("""Select * from  `tabGenerate Sales Unit`
		where project_name=%s  and phase_name=%s and building_name=%s and creation!=%s and docstatus!=%s""", (project,bill_of_material,building_name,creation,2), as_dict=True)
		
@frappe.whitelist()
def checkduplicatewithoutdate(project,bill_of_material,building_name):
	return frappe.db.sql("""Select * from  `tabGenerate Sales Unit`
	where project_name=%s  and phase_name=%s and building_name=%s and docstatus!=%s""", (project,bill_of_material,building_name,2), as_dict=True)

@frappe.whitelist()
def get_bill_of_material_count(parent, building_name):
	d = frappe.db.sql("""Select * from  `tabBill of Material Building Count`
	where parent=%s and building_name=%s""", (parent, building_name), as_dict=True)
	return d
	
# @frappe.whitelist()
# def insert_serial_no(serial_no,item_code,purchase_rate,company,warehouse,qty,qtypurchase_rate,item_name,cost_center,expense_act):
	# se = frappe.new_doc('Stock Entry')
	# se.purpose = "Material Receipt";
	# se.from_warehouse = warehouse;
	# se.company = company;
	# se.flags.ignore_mandatory = True;
	# se.append("items", {
	# "cost_center" : cost_center,
	# "expense_account" : expense_act,
	# "to_warehouse" : warehouse,
	# "t_warehouse" : warehouse,
	# "item_code" : item_code,
	# "item_name" : item_name,
	# "qty" : qty,
	# "transfer_qty" : qty,
	# "basic_rate" : purchase_rate,
	# "basic_amount" : qtypurchase_rate,
	# "amount" : qtypurchase_rate,
	# "valuation_rate" : purchase_rate,
	# "additional_cost" : 0,
	# "stock_uom" : "Nos",
	# "uom" : "Nos",
	# "conversion_factor" : 1,
	# "serial_no" : serial_no
	
	# })
	# se.submit()
	
@frappe.whitelist()
def insert_serial_nos(common_array,serial_array):
	se = frappe.new_doc('Stock Entry')
	se.purpose = "Material Receipt";
	se.from_warehouse = common_array["warehouse"];
	se.company = common_array["company"];
	se.flags.ignore_mandatory = True;
for key in serial_array:
    se.append("items", {
	"cost_center" : common_array["cost_center"],
	"expense_account" : common_array["expense_act"],
	"to_warehouse" : common_array["warehouse"],
	"t_warehouse" : common_array["warehouse"],
	"item_code" : key["type_item_code"],
	"item_name" : "BBSAP Single Story house (20' x 45')-EL",
	"qty" : key["type_qty"],
	"transfer_qty" : key["type_qty"],
	"basic_rate" : key["incoming_value"],
	"basic_amount" : key["incoming_value"],
	"amount" : key["incoming_value"],
	"valuation_rate" : key["incoming_value"],
	"additional_cost" : 0,
	"stock_uom" : "Nos",
	"uom" : "Nos",
	"conversion_factor" : 1,
	"serial_no" : key["serial_no"]
})
se.submit()	

@frappe.whitelist()
def get_item(name):
	d = frappe.db.sql("""Select * from  `tabItem Variant Attribute`
	where parent=%s """, (name), as_dict=True)
	return d
	
@frappe.whitelist()
def serial_delete(serialno):
		return frappe.db.sql("""Delete from `tabSerial No` where name=%s """,
			(serialno), as_dict=True)