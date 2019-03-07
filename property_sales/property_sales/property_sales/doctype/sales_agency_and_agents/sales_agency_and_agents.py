# -*- coding: utf-8 -*-
# Copyright (c) 2019, Tektician Sdn Bhd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint, _
from frappe.utils.nestedset import NestedSet

class RootNotEditable(frappe.ValidationError): pass
class BalanceMismatchError(frappe.ValidationError): pass

class SalesAgencyandAgents(NestedSet):
	nsm_parent_field = 'parent_agency'

	def before_insert(self):
		if self.create_agent_account:
			d=frappe.db.sql("""select email from  `tabUser` where email=%s""", self.email_address, as_dict=True)
			if d:
				frappe.msgprint(_(self.email_address+" is already recorded for a user, enter different Email"))
			else:
				doc = frappe.new_doc("User")
				doc.update({
		        "email":self.email_address,
		        "full_name":self.agent_full_name,
		        "send_welcome_email":1})
		        doc.save()
            
            	
            	
		        
	            


            	
                
                	

            	
	