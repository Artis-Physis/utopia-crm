# coding=utf-8
from datetime import date

from django.utils.translation import ugettext_lazy as _
from django.core.management import BaseCommand
from django.conf import settings

from support.models import Issue


DEFAULT_NOTE = _("Generated automatically on {}\n".format(date.today()))


class Command(BaseCommand):
    help = """Cierra incidencias de facturación de tipo gestión de cobranzas, automáticamente."""

    # This is left blank if it's necessary to add some arguments
    # def add_arguments(self, parser):
    #    # parser.add_argument('payment_type', type=str)

    def handle(self, *args, **options):
        # TODO: Generate a queryset to look for debtors, or a method to check for it while iterating through all
        # The first part would be faster probably
        issues = Issue.objects.filter(subcategory='I06').exclude(status__slug=settings.SOLVED_ISSUE_STATUS_SLUG)
        print(_("Started process"))
        for issue in issues.iterator():
            try:
                contact = issue.contact
                if contact.is_debtor() is False:  # No open issues with category I
                    print(_("Closing issue {} for contact {}. All their invoices are paid".format(
                        issue.id, contact.id)))
                    if not issue.progress:
                        issue.progress = ""
                    issue.progress = issue.progress + u"\nIncidencia cerrada automáticamente el {}".format(
                        date.today())
                    issue.closing_date = date.today()
                    issue.mark_solved()
                    issue.save()
            except Exception as e:
                print("Error issue {}, contact {}: {}".format(issue.id, contact.id, e.message))
        print(_("Ended process"))