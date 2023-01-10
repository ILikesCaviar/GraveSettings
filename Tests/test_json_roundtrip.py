from unittest import main
from io import StringIO

from grave_settings.formatters.json import JsonFormatter
from grave_settings.semantics import AutoPreserveReferences
from integrated_tests import TestRoundTrip


class TestJsonRoundtrip(TestRoundTrip):
    def get_formatter(self, serialization=True) -> JsonFormatter:
        formatter = JsonFormatter()
        self.register_default_semantics(formatter)
        return formatter

    def get_ser_obj(self, formatter, obj, route):
        stringio = StringIO()
        formatter.to_buffer(obj, stringio, route=route)
        stringio.seek(0)
        return stringio

    def formatter_deser(self, formatter, route, ser_obj: StringIO):
        return formatter.from_buffer(ser_obj, route=route)


if __name__ == '__main__':
    main()
