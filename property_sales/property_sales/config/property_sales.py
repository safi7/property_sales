from __future__ import unicode_literals
from frappe import _


def get_data():
	return [
		{
			"label": _("Project Sales Process"),
			"items": [
				{
					"type": "doctype",
					"label": _("Step 1: Create Item"),
					"name": "Item",
				},
				{
					"type": "doctype",
					"label": _("Step 2: Set Property Price"),
					"name": "Item Price",
				},
				{
					"type": "doctype",
					"label": _("Step 3: Generate Property for Sale"),
					"name": "Generate Sales Unit",
				},
				{
					"type": "doctype",
					"label": _("Step 4: Set Commission Scheme"),
					"name": "Commission Scheme",
				},
				{
					"type": "doctype",
					"label": _("Step 5: Create Property Sales Campaign"),
					"name": "Property Sales Campaign",
				},
				{
					"type": "doctype",
					"label": _("Step 6: Manage Sales Partner and Agents"),
					"name": "Sales Agency and Agents",
				},
				{
					"type": "doctype",
					"label": _("Step 7: Property Booking and Sales"),
					"name": "Property Sales",
				}
			],
			
		},
		{
			"label": _("Customer Relationship Management"),
			"items": [
				{
					"type": "doctype",
					"label": _("Leads Management"),
					"name": "Lead",
				},
				{
					"type": "doctype",
					"label": _("Customer Management"),
					"name": "Customer",
				}
			],
			
		},
		{
			"label": _("Items and Pricing"),
			"items": [
				{
					"type": "doctype",
					"name": "Item",
				},
				{
					"type": "doctype",
					"name": "Product Bundle",
				},
				{
					"type": "doctype",
					"name": "Price List",
				},
				{
					"type": "doctype",
					"name": "Item Group",
					"icon": "fa fa-sitemap",
					"label": _("Item Group"),
					"link": "Tree/Item Group",
				},
				{
					"type": "doctype",
					"name": "Item Price",
					"route": "List/Item Price"
				},
				{
					"type": "doctype",
					"name": "Shipping Rule",
				},
				{
					"type": "doctype",
					"name": "Pricing Rule",
				},
				{
					"type": "doctype",
					"name": "Item Variant Settings",
				},
			]
		},
		{
			"label": _("Sales Agency and Agents"),
			"items": [
				{
					"type": "doctype",
					"label": _("Sales Agency and Agents Management"),
					"name": "Sales Agency and Agents",
				},				
				{
					"type": "doctype",
					"label" : _("Commission Scheme"),
					"name": "Commission Scheme",
				},						
				{
					"type": "doctype",
					"label" : _("Property Disbursement Schedule"),
					"name": "Property Disbursement Schedule",					
				},				
			]
		},
		{
			"label": _("Property Inventory"),
			"items": [
				{
					"type": "doctype",
					"label" : _("Generate Sales Unit"),
					"name": "Generate Sales Unit",
				},
				{
					"type": "doctype",
					"label" : _("Property Sales Inventory"),
					"name": "Serial No",
				},
			]
		}		
		]
	 
 


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/contract/css/contract.css"
# app_include_js = "/assets/contract/js/contract.js"

# include js, css files in header of web template
# web_include_css = "/assets/contract/css/contract.css"
# web_include_js = "/assets/contract/js/contract.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "contract.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "contract.install.before_install"
# after_install = "contract.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "contract.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"contract.tasks.all"
# 	],
# 	"daily": [
# 		"contract.tasks.daily"
# 	],
# 	"hourly": [
# 		"contract.tasks.hourly"
# 	],
# 	"weekly": [
# 		"contract.tasks.weekly"
# 	]
# 	"monthly": [
# 		"contract.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "contract.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "contract.event.get_events"
# }

