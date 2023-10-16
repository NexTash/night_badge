# Copyright (c) 2023, NexTash (SMC-PVT) Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Patient(Document):
	def autoname(self):
		pass
		# self.name  = self.full_name
	
	def validate(self):
		if frappe.db.exists("Patient", self.name):
			visits = self.visits
			
			if len(visits):
				date = visits[-1].date

				# create a new document
				doc = frappe.get_doc({
					'doctype': 'Patient Activity',
					'patient': self.name,
					"activity": f"Visited on {date}"
				})
				doc.insert()
	
	@frappe.whitelist()
	def dead(self):
		doc = frappe.get_doc({
			'doctype': 'Patient Activity',
			'patient': self.name,
			"activity": f"dEAD"
		})
		doc.insert()

	# def on_update(self):
	# 	frappe.msgprint(f"update")

	# def on_update_after_submit(self):
	# 	frappe.msgprint(f"update as")
	
	# def before_insert(self):
	# 	frappe.msgprint("Insert")

	# def on_submit(self):
	# 	frappe.msgprint("submit")

	# def on_cancel(self):
	# 	frappe.msgprint("Cancel")

	# def on_trash(self):
	# 	frappe.msgprint("Deleted")
