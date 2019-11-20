# -*- coding: utf-8 -*-
import codecs


keywords = {
    "Sant": "True",
    "Falskt": "False",
    "om": "if",
    "for": "för",
    "while": "medans",
    "print": "skriv",
    "abs": "belopp",
    "all": "alla",
    "open": "öppna",
    "sum": "summa",
    "float": "flyttal",
    "max": "störst",
    "min": "minst",
    "list": "lista",
    "dict": "katalog",
    "with": "med",
    "reduce": "förvandla",
    "map": "mappa",
    "filter": "filtrera",
    "sorted": "ordnad",
    "str": "sträng",
    "int": "tal",
}


class SwedishCodec(codecs.Codec):
    def encode(self, data, errors="strict"):
        return (data.encode("utf8"), len(data))

    def decode(self, data, errors="strict"):
        data_string = codecs.decode(data, "utf8")

        for remapped, real in keywords.items():
            data_string = data_string.replace(remapped, real)

        return (data_string, len(data))


class SwedishIncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return SwedishCodec().encode(input)


class SwedishIncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return SwedishCodec().decode(input)


class SwedishStreamReader(SwedishCodec, codecs.StreamReader):
    pass


class SwedishStreamWriter(SwedishCodec, codecs.StreamWriter):
    pass


def search(encoding):
    if encoding != "swedish":
        return None

    return codecs.CodecInfo(
        name="swedish",
        encode=SwedishCodec().encode,
        decode=SwedishCodec().decode,
        incrementalencoder=SwedishIncrementalEncoder,
        incrementaldecoder=SwedishIncrementalDecoder,
        streamreader=SwedishStreamReader,
        streamwriter=SwedishStreamWriter,
    )


codecs.register(search)
