# Copyright (c) 2023, edom ibrahim and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CustomerVisits(Document):
	def on_change(self):
		update_all_re_by_id(self.customer_record_number)


		


	
	
	

def update_all_re_by_id(customer_record_number):
		visits = frappe.db.get_list('Customer Visits',
						filters={
					'customer_record_number':customer_record_number
				},
		fields=['name','customer_record_number']
		)

		for v in visits:
			count = frappe.db.count('Customer Visits',
						filters={
							'status_schedule': 'Scheduled',
							'customer_record_number':v.customer_record_number
						})
			frappe.db.set_value('Customer Visits', v.name, 'remaining_visits', count, update_modified=False)
		frappe.db.commit()



		



	  
	

def update_all_re():
		visits = frappe.db.get_list('Customer Visits',
		fields=['name','customer_record_number']
		)

		for v in visits:
			count = frappe.db.count('Customer Visits',
						filters={
							'status_schedule': 'Scheduled',
							'customer_record_number':v.customer_record_number
						})
			frappe.db.set_value('Customer Visits', v.name, 'remaining_visits', count, update_modified=False)
		frappe.db.commit()



		



