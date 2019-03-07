// Copyright (c) 2019, Tektician Sdn Bhd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Commission Scheme', {
	refresh: function(frm) {
     
  
	},
	before_commission_scheme_remove: function(frm, cdt, cdn) {
        console.log("test1");
    },
onload: function(frm) {
     if(cur_frm.doc.disbursement_schedule_com){
     	getNamesDescription(frm)

     }
  
	},
 disbursement_schedule_com:function(frm,cdt,cdn) {
    getNamesDescription(frm,cdt,cdn)
  
  }
});

function getNamesDescription(frm){
	


var d1 =  {   
              "parent": cur_frm.doc.disbursement_schedule_com 
         };   
frappe.call({
    method: "property_sales.property_sales.doctype.commission_scheme.commission_scheme.get_names",
             args: d1,
    callback: function(r) {

frappe.meta.get_docfield('Commission Scheme Schedule', 'disbursement_schedule',cur_frm.doc.name).options 
= r.message;
frm.refresh_field('disbursement_schedule');
 			}
    });

}


frappe.ui.form.on("Commission Scheme Schedule", {

	disbursement_schedule: function(frm, cdt, cdn){
		var row=locals[cdt][cdn];
frappe.call({
    method: "property_sales.property_sales.doctype.commission_scheme.commission_scheme.get_description",
              freeze: true,
             args: {
             	parent: cur_frm.doc.disbursement_schedule_com,
             	name1: row.disbursement_schedule
             },
    callback: function(r) {

     if(r.message){
     	
     	row.disbursement_description=r.message[0].descs;
     	cur_frm.refresh_field("commission_scheme");
        
     }
	}

});


},

before_commission_scheme_remove: function(frm, cdt, cdn) {
     console.log(cur_frm.doc.disbursement_schedule_com);
        cur_frm.disbursement_schedule_com=cur_frm.doc.disbursement_schedule_com;
        cur_frm.refresh_field("disbursement_schedule_com");

    }
});

