# Copyright (c) 2023, edom ibrahim and contributors
# For license information, please see license.txt
from frappe.utils import today,getdate
from datetime import datetime
import frappe
from frappe.model.document import Document

class Target(Document):
	pass






@frappe.whitelist()
def getTarget(id):
	total_sales= 0
	sales_amount_due = 0
	subscriptions_amount_due = 0
	doc = frappe.get_doc('Target', id)
	shifts=frappe.db.get_list('POS Closing Shift',filters=[
		
				['posting_date', 'between', [doc.from_date, doc.to_date]],
				['user', '=', doc.seller],

		],fields=['*'])
	for sh in shifts:
		total_sales += sh.net_total

	# total_sales = 1500
	frappe.db.set_value('Target', id, {
					'total_sales': total_sales ,
					'sales_amount_due': sales_amount_due,
					'subscriptions_amount_due':subscriptions_amount_due,
					'subscriptions_amount_due':subscriptions_amount_due,
					'percentage': (total_sales / doc.goal) * 100,
					'sales_amount_due': 0.0,
					'subscriptions_amount_due': 0.0

					})
	frappe.db.commit()
	doc2 = frappe.get_doc('Target', id)
	percentage_emp = doc2.percentage

	percentages =  frappe.get_all("Target Percentages", filters = dict(parent=id), 
		fields = ["*"],order_by='percentage desc',)
	for p in percentages:
		frappe.db.set_value('Target Percentages', p.name, {
				'achieved_goal': False ,
			})
		frappe.db.commit()

	for p in percentages:
		if percentage_emp >= p.percentage:
			frappe.db.set_value('Target Percentages', p.name, {
				'achieved_goal': True ,
			})
			frappe.db.set_value('Target', id, {
					'sales_amount_due': (total_sales / 100) * p.due

					})
			frappe.db.commit()
			break


	all_subscriptions =  frappe.get_all("Target Subscriptions", filters = dict(parent=id), 
									fields = ["*"])
	for sub in all_subscriptions:
		print("88888888888888888")
		frappe.db.set_value('Target Subscriptions', sub.name, {
		'number_of_sale': 0,
		'total': 0})
		frappe.db.commit()






    

		#==== get invoices
	shifts2=frappe.db.get_list('POS Closing Shift',filters=[
		
				['posting_date', 'between', [doc.from_date, doc.to_date]],
				['user', '=', doc.seller],

		],fields=['*'])
	print(shifts2)
	for shif in shifts2:
		get_invoices =  frappe.get_all("Sales Invoice", filters = [
			["posa_pos_opening_shift","=" ,shif.pos_opening_shift],
			["status","=","Paid"]
		], 
		fields = ["*"])
		print('1111111111111111111111111111111111')
		for inv in get_invoices:
			all_items = frappe.get_all("Sales Invoice Item", filters = dict(parent=inv.name), 
										fields = ["*"])
			for item in all_items:
				subscriptions =  frappe.get_all("Target Subscriptions", filters = dict(parent=id), 
												fields = ["*"])
				for sub in subscriptions:
					if item.item_code == sub.item:
						number_sales = sub.number_of_sale +1
						frappe.db.set_value('Target Subscriptions', sub.name, {
						'number_of_sale': number_sales,
						'total': sub.due * number_sales

						})
						frappe.db.commit()
	


	doc2 = frappe.get_doc('Target', id)
	total_sub = 0
	for rec in doc2.subscriptions:
		total_sub += rec.total

	frappe.db.set_value('Target', id, {
					'subscriptions_amount_due': total_sub

					})
	frappe.db.commit()				

			




				

			
		
				
			


		






