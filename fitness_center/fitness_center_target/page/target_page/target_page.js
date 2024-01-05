frappe.pages['target-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Target',
		single_column: true
	});

	targets = []


	frappe.db.get_list('Target', {
		fields: ['*'],
		filters: {
			// "seller":"abolu"
			
		}
	}).then(records => {
		targets = records
		console.log(records);
	})


	$(frappe.render_template('target_page', {"targets": targets}))
	.appendTo(page.body);
}