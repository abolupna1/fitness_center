# Copyright (c) 2023, edom ibrahim and contributors
# For license information, please see license.txt
from frappe.utils import add_to_date
from frappe.utils import today,getdate
from datetime import datetime

import frappe
from frappe.model.document import Document

class CustomerSubscriptions(Document):
    def before_insert(self):
        self.appointments = []
        dates = []
        d = self.start
        end = add_to_date(d, months=self.month_cont)
        m_count = (getdate(end) - getdate(d)).days / 7
        for i in range(int(m_count)):
            if d > today():
                vis={"date":d,"time":self.scheduled_time,"day":self.scheduled_day}
                dates.append(vis)
            scd = self.append("appointments",{
                'scheduled_date': d,
                'scheduled_time':self.scheduled_time,
                'scheduled_day' : self.scheduled_day
            })
            self.end=d
            d =add_to_date(d, days=7)
        records=frappe.db.get_list('Customer Visits', filters=[
            ['scheduled__date', 'between', [add_to_date(today(), days=1),self.end]],
            ['status_schedule', '=', "Scheduled"],
            ['customer_record_number', '=', self.customer_record_number],
            ])
        for rec in records:
            frappe.db.delete('Customer Visits',rec['name'])
        
        for rec in dates:
            vsit=frappe.new_doc("Customer Visits")
            vsit.status = 'Subscription'
            vsit.scheduled__date = rec['date']
            vsit.scheduled_time = rec['time']
            vsit.scheduled_day = rec['day']
            vsit.status_schedule = "Scheduled"
            vsit.customer_record_number = self.customer_record_number
            vsit.insert()

    def on_update(self):
        self.appointments = []
        dates = []
        d = self.start
        end = add_to_date(d, months=self.month_cont)
        m_count = (getdate(end) - getdate(d)).days / 7
        for i in range(int(m_count)):
            if d > today():
                vis={"date":d,"time":self.scheduled_time,"day":self.scheduled_day}
                dates.append(vis)
            scd = self.append("appointments",{
                'scheduled_date': d,
                'scheduled_time':self.scheduled_time,
                'scheduled_day' : self.scheduled_day
			})
            self.end=d
            d =add_to_date(d, days=7)
            
       
        records=frappe.db.get_list('Customer Visits', filters=[
            ['scheduled__date', 'between', [add_to_date(today(), days=1),self.end]],
            ['status_schedule', '=', "Scheduled"],
            ['customer_record_number', '=', self.customer_record_number],
            ])
        for rec in records:
            frappe.db.delete('Customer Visits',rec['name'])
        
        for rec in dates:
            vsit=frappe.new_doc("Customer Visits")
            vsit.status = 'Subscription'
            vsit.scheduled__date = rec['date']
            vsit.scheduled_time = rec['time']
            vsit.scheduled_day = rec['day']
            vsit.status_schedule = "Scheduled"
            vsit.customer_record_number = self.customer_record_number
            vsit.insert()




        




  #  def after_insert(self):
   #         records=frappe.db.get_list("Customer Records")
   #         vsit=frappe.new_doc("Customer Visits")
    #        vsit.status = 'Free'
      #      vsit.customer_record_number = self.name
         #   vsit.insert()

        
   
     
              

        
        
        


      

	
