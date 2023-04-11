import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(path, "r") as file:
            result = file.read()
            read_data = xmltodict.parse(result)["dataset"]["record"]
            return read_data
