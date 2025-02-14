// Copyright (c) 2025, Augusto Lorencatto and contributors
// For license information, please see license.txt

frappe.ui.form.on("Cardapio", {
	refresh(frm) {

        frm.add_custom_button(__('Teste de botão'), () => {
            // frm.add_child('phone', {
            //     phone: ''
            // })
            // frm.refresh_field('phone');

            // frappe.msgprint({
            //     title: __('Notificação'),
            //     indicator: 'green',
            //     message: __('Aqui uma notificação')
            // });

            frappe.show_alert({
                message:__('Mensagem de teste...'),
                indicator:'blue' // blue | green
            }, 5);
            
            // Disparando ação
            frm.call('dispara_integracao')
                .then(r => {
                    console.log(`Aqui a resposta : ${r.message.chave}`)
                })
            
        },__("Ações"))

	},
});
