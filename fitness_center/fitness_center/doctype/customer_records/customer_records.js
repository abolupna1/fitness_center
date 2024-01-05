// Copyright (c) 2023, edom ibrahim and contributors
// For license information, please see license.txt

frappe.ui.form.on('Customer Records', {
	health_problems: function(frm) {
		frm.set_df_property('health_issues', 'reqd', frm.doc.health_problems)
	},

	surgery: function(frm) {
		frm.set_df_property('surgeries', 'reqd', frm.doc.surgery)
	},

	taking_medications: function(frm) {
		frm.set_df_property('medicines', 'reqd', frm.doc.taking_medications)
	}
});
