// Copyright (c) 2023, edom ibrahim and contributors
// For license information, please see license.txt

frappe.ui.form.on('Customer Subscriptions', {



	 refresh: function(frm) {
		frm.set_df_property('invoice_number', 'only_select', true);
	}






});


