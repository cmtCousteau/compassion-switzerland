# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Compassion CH (http://www.compassion.ch)
#    Releasing children from poverty in Jesus' name
#    @author: Emanuel Cino <ecino@compassion.ch>
#
#    The licence is in the file __manifest__.py
#
##############################################################################

import logging


from odoo import api, models

logger = logging.getLogger(__name__)


class ReportChildpackFull(models.AbstractModel):
    """
    Model used to generate childpack in selected language
    """
    _name = 'report.report_compassion.childpack_full'

    def _get_report(self):
        return self.env['report']._get_report_from_name(
            'report_compassion.childpack_full')

    @api.multi
    def render_html(self, docids, data=None):
        """
        :param data: data collected from the print wizard.
        :return: html rendered report
        """
        if not data:
            data = {}
        lang = data.get('lang', self.env.lang)
        report = self._get_report()
        docs = self.env[report.model].with_context(lang=lang).browse(docids)

        data.update({
            'doc_model': report.model,
            'docs': docs.with_context(lang=lang)
        })

        return self.env['report'].with_context(lang=lang).render(
            report.report_name, data)


# pylint: disable=R7980
class ReportChildpackSmall(models.AbstractModel):
    _inherit = 'report.report_compassion.childpack_full'
    _name = 'report.report_compassion.childpack_small'

    def _get_report(self):
        return self.env['report']._get_report_from_name(
            'report_compassion.childpack_small')


class ReportChildpackMini(models.AbstractModel):
    _inherit = 'report.report_compassion.childpack_full'
    _name = 'report.report_compassion.childpack_mini'

    def _get_report(self):
        return self.env['report']._get_report_from_name(
            'report_compassion.childpack_mini')
