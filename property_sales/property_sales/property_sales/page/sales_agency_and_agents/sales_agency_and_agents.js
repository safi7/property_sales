
frappe.pages['sales-agency-and-agents'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Sales Agency And Agents Tree',
		single_column: true
	});

wrapper.page.add_menu_item(__('List View'), function() {
			window.location.href='/desk#List/Sales%20Agency%20and%20Agents/List';
		});

wrapper.page.add_menu_item(__('Refresh'), function() {
			wrapper.make_tree();
		});

	wrapper.make_tree = function() {
		var ctype = frappe.get_route()[1] || 'Sales Agency and Agents';
		return frappe.tree_chart = new frappe.TreeChart(ctype, "Sales Agency and Agents", page,
					    page.main.css({
						"min-height": "300px",
						"padding-bottom": "25px"
					}));
	}

	wrapper.make_tree();

	}

frappe.pages['sales-agency-and-agents'].on_page_show = function(wrapper){
	// set route
	
	var ctype = frappe.get_route()[1] || 'Sales Agency and Agents';

	wrapper.page.set_title(__('{0} Chart',[__(ctype)]));

	if(frappe.tree_chart && frappe.tree_chart.ctype != ctype) {
		wrapper.make_tree();
	}

	frappe.breadcrumbs.add(frappe.breadcrumbs.last_module || "Property Sales");
};

frappe.TreeChart = Class.extend({
	init: function(ctype, root, page, parent) {
		$(parent).empty();
		var me = this;
		me.ctype = ctype;
		me.page = page;
		
		
		me.can_read = frappe.model.can_read(this.ctype);
		me.can_create = frappe.boot.user.can_create.indexOf(this.ctype) !== -1 ||
					frappe.boot.user.in_create.indexOf(this.ctype) !== -1;
		me.can_write = frappe.model.can_write(this.ctype);
		me.can_delete = frappe.model.can_delete(this.ctype);

		me.page.set_primary_action(__("New"), function() {
			me.new_node();
		
	}, "octicon octicon-plus");

		this.tree = new frappe.ui.Tree({
			parent: $(parent),
			label: __(root),
			
			method: 'property_sales.property_sales.page.sales_agency_and_agents.sales_agency_and_agents.get_nodes'
			,
			toolbar: [
				{toggle_btn: true},
				{
					label:__("Edit"),
					condition: function(node) {
						return !node.root && me.can_read && node.label!="Sales Agency and Agents";
					},
					click: function(node) {
						frappe.set_route("Form", me.ctype, node.label);
						//console.log("Edit")

					}
				},
				{
					label:__("Add Child"),
					condition: function(node) { return me.can_create && node.expandable; },
					click: function(node) {
						me.new_node();
						console.log(me.can_create+" "+ node.expandable);
					},
					btnClass: "hidden-xs"
				},
				{
					label:__("Rename"),
					condition: function(node) { return !node.root && me.can_write && node.label!="Sales Agency and Agents"; },
					click: function(node) {
						console.log(node.label);
						frappe.model.rename_doc(me.ctype, node.label, function(new_name) {
							node.$a.html(new_name);

						});
					},
					btnClass: "hidden-xs"
				},
				{
					label:__("Delete"),
					condition: function(node) { return !node.root && me.can_delete && node.label!="Sales Agency and Agents"; },
					click: function(node) {
						frappe.model.delete_doc(me.ctype, node.label, function() {
							node.parent.remove();
						});
					},
					btnClass: "hidden-xs"
				}

			]
		});
	},
	new_node: function() {
		var me = this;
		var node = me.tree.get_selected_node();

		var parent_agency=node.label;
	
		if(!(node && node.expandable)) {
			frappe.msgprint(__("Select a group node first."));
			return;
		}

		var fields = [
			{fieldtype:'Data', fieldname: 'agent_full_name',
				label:__('Agent/Agency Full Name',[__(me.ctype)]), reqd:true},
			{fieldtype:'Data', fieldname: 'email_address',
				label:__('Email Address',[__(me.ctype)])},
			{fieldtype:'Check', fieldname:'create_agent_account', label:__('Create Agent/Agency Account',[__(me.ctype)])},
			
			{fieldtype:'Check', fieldname:'is_group', label:__('Is Agency',[__(me.ctype)]),
				description: __("Further nodes can be only created under 'Group' type nodes")},
			{fieldtype:'Small Text', fieldname:'address', label:__('Address',[__(me.ctype)])},
			{fieldtype:'Data', fieldname: 'mobile_phone',
				label:__('Mobile Phone',[__(me.ctype)])},
			{fieldtype:'Data', fieldname: 'ic_number',
				label:__('IC or Passport Number',[__(me.ctype)])}

				]


		// the dialog
		var d = new frappe.ui.Dialog({
			title: __('New {0}',[__(me.ctype)]),
			fields: fields
		})
      
		d.set_value("is_group", "No");

		// create
		d.set_primary_action(__("Create New"), function() {
			var btn = this;
			 console.log(parent_agency);
			var v=d.get_values();

			v["parent_agency"]=parent_agency;
			console.log(v);
			if(!v) return;

			var node = me.tree.get_selected_node();

			v.parent = node.label;
			v.ctype = me.ctype;

			return frappe.call({
				method: 'property_sales.property_sales.page.sales_agency_and_agents.sales_agency_and_agents.add_node',
				args: v,
				callback: function(r) {
					if(!r.exc) {
						d.hide();
						if(node.expanded) {
							//node.toggle_node();
						}
						window.location.reload();
					}
				}
			});
		});

		d.show();
	},
});