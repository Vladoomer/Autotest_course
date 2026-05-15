import xml.etree.ElementTree as ET

xml_data = """
<person>
    <id>1</id>
    <name>Vlad</name>
    <email>vlad@gmail.com</email>
    <age>30</age>
    <address>
        <city>New York</city>
        <street>Main street</street>
        <zip>109080</zip>
    </address>
</person>"""

root = ET.fromstring(xml_data)