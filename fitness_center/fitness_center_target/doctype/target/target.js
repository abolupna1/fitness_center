// Copyright (c) 2023, edom ibrahim and contributors
// For license information, please see license.txt

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
}
});



// $(".ellipsis").on("click",  function() {

// 	console.log("mode")

// });
