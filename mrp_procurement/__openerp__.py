# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    "name" : "Procurements",
    "version" : "1.0",
    "author" : "Tiny",
    "website" : "http://www.openerp.com",
    "category" : "Generic Modules/Production",
    "depends" : ["base","process", "product", "stock"],
    "description": """
    This is the module for computing Procurements.
    """,
    'init_xml': [],
    'update_xml': [
        'security/ir.model.access.csv',
        'security/mrp_procurement_security.xml',
        'mrp_procurement_data.xml',
        'wizard/make_procurement_view.xml',
        'wizard/mrp_procurement_view.xml',
        'wizard/orderpoint_procurement_view.xml',
        'mrp_procurement_view.xml',
        'wizard/schedulers_all_view.xml',
        'mrp_procurement_workflow.xml',
        'process/procurement_process.xml',
        "company_view.xml",
    ],
#    'demo_xml': [],
    'installable': True,
    'active': False,
    'certificate': '',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
