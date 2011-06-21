from django.core.management.base import LabelCommand
from django.db.models.loading import get_model

class Command(LabelCommand):
    help = "Prints xmlpipe2 source for given model."

    def handle_label(self, label, **kwargs):
        from djangosphinx.utils.config import print_xml_source_for_model
        print_xml_source_for_model(get_model(*label.split('.')))

