from __future__ import unicode_literals
import frappe


# @frappe.whitelist()
# def get_children():
# 	ctype = frappe.local.form_dict.get('ctype')
# 	parentfield = 'parentfield' 
# 	parent = frappe.form_dict.get("parent") or ""

# 	return frappe.db.sql("""select name as value,
# 		if(is_group='yes',1,0) as expandable
# 		from `tabSales Agency and Agents`
# 		where docstatus < 2
# 		and ifnull(`{parentfield}`,'') = %s
# 		order by name""".format(ctype=frappe.db.escape(ctype), parentfield=frappe.db.escape(parentfield)),
# 		parent, as_dict=1)


@frappe.whitelist()
def get_nodes(parent=None, parent_agency=None, is_root=False):
	if parent is None or parent == "Sales Agency and Agents":
		parent = ""
	return frappe.get_all("Sales Agency and Agents", fields=["name as value", "is_group as expandable"], filters={"parent_agency": parent})
   

@frappe.whitelist()
def add_node():
	ctype = frappe.form_dict.get('ctype')
	parent_field = 'parent_agency' 
	

	doc = frappe.new_doc(ctype)
	if frappe.form_dict['parent_agency']=="Sales Agency and Agents":
		doc.update({
		"agent_full_name": frappe.form_dict['agent_full_name'],
		"email_address": frappe.form_dict['email_address'],
		"create_agent_account": frappe.form_dict['create_agent_account'],
		"is_group": frappe.form_dict['is_group'],
		"address": frappe.form_dict['address'],
		"mobile_phone": frappe.form_dict['mobile_phone'],
		"ic_number": frappe.form_dict['ic_number']
	})
    
	else:
		doc.update({
		"agent_full_name": frappe.form_dict['agent_full_name'],
		"email_address": frappe.form_dict['email_address'],
		"create_agent_account": frappe.form_dict['create_agent_account'],
		"is_group": frappe.form_dict['is_group'],
		"address": frappe.form_dict['address'],
		"mobile_phone": frappe.form_dict['mobile_phone'],
		"ic_number": frappe.form_dict['ic_number'],
		"parent_agency": frappe.form_dict['parent_agency']
	})
		
	doc.save()
