import base64
import binascii
import asn1
import asn1tools

declaration = """[module]DEFINITIONS [tags] ::= BEGIN
[linkage]
[declarations]
END"""

def pretty_print(input_stream, output_stream, indent=0):
    """Pretty print ASN.1 data."""
    while not input_stream.eof():
        tag = input_stream.peek()
        if tag.typ == asn1.TypePrimitive:
            tag, value = input_stream.read()
            output_stream.write(' ' * indent)
            output_stream.write('[{}] {}: {}\n'.format(class_id_to_string(tag.cls),
                                                       tag_id_to_string(tag.nr), value_to_string(tag.nr, value)))
        elif tag.typ == asn1.TypeConstructed:
            output_stream.write(' ' * indent)
            output_stream.write('[{}] {}\n'.format(class_id_to_string(tag.cls),
                                                   tag_id_to_string(tag.nr)))
            input_stream.enter()
            pretty_print(input_stream, output_stream, indent + 2)
            input_stream.leave()

f = open('chiave.pem')
b64key = ""
for line in f:
    if '---' in line:
        continue
    else:
        b64key = b64key + line[:-1]

print(b64key)
bytess = base64.b64decode(b64key)
print(bytess)

foo = asn1tools.compile_string(declaration)
#foo = asn1tools.compile_files('tests/files/foo.asn', 'per')
encoded = foo.encode('Question', {'id': 1, 'question': 'Is 1+1=3?'})
res = foo.decode('value', bytess)
print(res)