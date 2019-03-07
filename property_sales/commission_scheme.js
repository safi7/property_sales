// Copyright (c) 2019, Tektician Sdn Bhd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Commission Scheme', {
	refresh: function(frm) {
        console.log("working");
	},
	disbursement_schedule:function(frm,cdt,cdn) {
    
   getNamesDescription(frm,cdt,cdn);
  }
});

function getNamesDescription(frm,cdt,cdn){
    var row = locals[cdt][cdn];
	   frappe.call({
            method: 'property_sales.property_sales.doctype.commission_scheme.commission_scheme.get_names_description',
            freeze: true,
            args: {
              parent: cur_frm.doc.disbursement_schedule
            },
            callback: function(r){
               
              if (r.message) {
                console.log(r.message);
                $.each(r.message, function(i, rowt) {


             
                });
              }
            }
          });
}