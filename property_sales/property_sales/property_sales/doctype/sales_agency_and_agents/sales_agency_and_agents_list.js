
frappe.listview_settings['Sales Agency and Agents'] = {
	onload: function(me) {
		
		
		//me.page.set_title(__("To Do"));
		me.page.add_sidebar_item(__("Tree"), function() {
			window.location.href='/desk#sales-agency-and-agents';
			
		});

		
	}


}