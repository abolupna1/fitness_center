// Copyright (c) 2023, edom ibrahim and contributors
// For license information, please see license.txt
frappe.ui.form.on("Target", "onload", function(frm) {
    frm.set_query("bank_account", function() {
        return {
            "filters": {
                "account_type": "Bank",
            }
        };
    });
});

frappe.ui.form.on('Target', {




    refresh: function(frm) {


   
      frm.add_custom_button(__('Update Target'), function(){







	

	

		frappe.call({
			args: {
				"id":frm.selected_doc.name,
			
			},
			method: "fitness_center.fitness_center_target.doctype.target.target.getTarget", //dotted path to server method
			
			callback: function(r) {
				// code snippet
				frm.reload_doc();

			}
		});
    });
   
  },
  after_save(frm) {
	frappe.call({
		args: {
			"id":frm.selected_doc.name,
		
		},
		method: "fitness_center.fitness_center_target.doctype.target.target.getTarget", //dotted path to server method
		
		callback: function(r) {
			// code snippet
			frm.reload_doc();

		}
	});
},

// onload: function(frm) {
// 	console.log(frappe.user.has_role('Target Employee'))
// 	if(frappe.user.has_role('Target Employee')){
		
// 		frm.disable_save();
// 		frm.set_df_property('percentages', 'cannot_add_rows', true);

	





// 	frm.set_df_property('seller,', 'read_only', frm.doc.__islocal ? 0 : 1);
// 	}
// 	},





},


);


