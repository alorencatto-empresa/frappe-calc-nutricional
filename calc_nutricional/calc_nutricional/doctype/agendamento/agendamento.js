// Copyright (c) 2025, Augusto Lorencatto and contributors
// For license information, please see license.txt

frappe.ui.form.on("Agendamento", {
	refresh(frm) {

        frm.add_custom_button(__('Gerar relatório'), () => {
            frappe.show_alert({
                message:__('Mensagem de teste...'),
                indicator:'blue' // blue | green
            }, 5);
        })

	},
});
