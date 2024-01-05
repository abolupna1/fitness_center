// Copyright (c) 2023, edom ibrahim and contributors
// For license information, please see license.txt
// frappe.listview_settings['Customer Visits'] = {

//     get_indicator(doc) {
//         // customize indicator color
//         if (doc.status_schedule = 'Finish') {
//             return [__("Finish"), "green", "status_schedule,=,Finish"];
//         } 
//     },

// }
frappe.ui.form.on('Customer Visits', {
	refresh: function(frm) {
		if (!frm.is_new()) {
			frm.add_custom_button(__('Finish'), function(){
				frm.set_value({
					status_schedule: 'Finish',
				})
				
						frm.save();
			
					});
		}

		frm.set_df_property('customer_record_number', 'only_select', true);


	}
});
