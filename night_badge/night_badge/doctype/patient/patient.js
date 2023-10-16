// Copyright (c) 2023, NexTash (SMC-PVT) Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Patient', {
	refresh(frm) {
		frm.add_custom_button('Dead', () => {
			frm.call("dead")	
		});
	},
	cnic_no: function(frm) {
		console.log('Lol 🎉 ');
	},
});

frappe.ui.form.on('Visits', {
	before_visits_remove(frm, cdt, cdn) {
		let date = locals[cdt][cdn].date
		console.log(`A row is about to removed 🎉 ${date}`);
	},
	
	visits_remove(frm, cdt, cdn) {
		console.log(`A row is removed 🎉`);
	},

	visits_add(frm, cdt, cdn) {
		console.log(`A row is added 🎉`);
	},

	visits_move(frm, cdt, cdn) {
		console.log(`A row is moved 🎉`);
	},

	form_render(frm, cdt, cdn) {
		console.log(`A form is rendered 🎉`);
	},

	date: function(frm) {
		console.log('Lol Date 🎉 ');
	}
});