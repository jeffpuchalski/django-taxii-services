
# BaseXMLQueryHandler generated by generate_xml_query_extension.py

import taxii_services.taxii_handlers.BaseXmlQueryHandler as BaseXmlQueryHandler
import taxii_services.handlers as h

class Stix111QueryHandler(BaseXMLQueryHandler):
    supported_targeting_expression = 'urn:stix.mitre.org:xml:1.1.1'
    mapping_dict = {'root_context': {'children': {'STIX_Package': {'has_text': False, 'namespace': 'http://stix.mitre.org/stix-1', 'prefix': 'stix', 'children': {'Threat_Actors': {'has_text': False, 'namespace': 'http://stix.mitre.org/stix-1', 'prefix': 'stix', 'children': {'Threat_Actor': {'has_text': False, 'namespace': 'http://stix.mitre.org/stix-1', 'prefix': 'stix', 'children': {'Identity': {'has_text': False, 'namespace': 'http://stix.mitre.org/ThreatActor-1', 'prefix': 'threat-actor', 'children': {'Specification': {'has_text': False, 'namespace': 'http://stix.mitre.org/extensions/Identity#CIQIdentity3.0-1', 'prefix': 'stix-ciq', 'children': {'Languages': {'has_text': False, 'namespace': 'urn:oasis:names:tc:ciq:xpil:3', 'prefix': 'xpil', 'children': {'Language': {'has_text': True, 'namespace': 'urn:oasis:names:tc:ciq:xpil:3', 'prefix': 'xpil', 'children': None}}}, 'PartyName': {'has_text': False, 'namespace': 'urn:oasis:names:tc:ciq:xpil:3', 'prefix': 'xpil', 'children': {'OrganisationName': {'has_text': False, 'namespace': 'urn:oasis:names:tc:ciq:xnl:3', 'prefix': 'xnl', 'children': {'NameElement': {'has_text': True, 'namespace': 'urn:oasis:names:tc:ciq:xnl:3', 'prefix': 'xnl', 'children': None}}}}}, 'Addresses': {'has_text': False, 'namespace': 'urn:oasis:names:tc:ciq:xpil:3', 'prefix': 'xpil', 'children': {'Address': {'has_text': False, 'namespace': 'urn:oasis:names:tc:ciq:xpil:3', 'prefix': 'xpil', 'children': {'Country': {'has_text': False, 'namespace': 'urn:oasis:names:tc:ciq:xal:3', 'prefix': 'xal', 'children': {'NameElement': {'has_text': True, 'namespace': 'urn:oasis:names:tc:ciq:xal:3', 'prefix': 'xal', 'children': None}}}}}}}}}, 'Role': {'has_text': True, 'namespace': 'http://stix.mitre.org/extensions/Identity#CIQIdentity3.0-1', 'prefix': 'stix-ciq', 'children': None}}}}}}}, 'STIX_Header': {'has_text': False, 'namespace': 'http://stix.mitre.org/stix-1', 'prefix': 'stix', 'children': {'Information_Source': {'has_text': False, 'namespace': 'http://stix.mitre.org/stix-1', 'prefix': 'stix', 'children': {'References': {'has_text': False, 'namespace': 'http://stix.mitre.org/common-1', 'prefix': 'stixCommon', 'children': {'Reference': {'has_text': True, 'namespace': 'http://stix.mitre.org/common-1', 'prefix': 'stixCommon', 'children': None}}}, 'Contributing_Sources': {'has_text': False, 'namespace': 'http://stix.mitre.org/common-1', 'prefix': 'stixCommon', 'children': {'Source': {'has_text': False, 'namespace': 'http://stix.mitre.org/common-1', 'prefix': 'stixCommon', 'children': {'Role': {'has_text': True, 'namespace': 'http://stix.mitre.org/common-1', 'prefix': 'stixCommon', 'children': None}, 'Identity': {'has_text': False, 'namespace': 'http://stix.mitre.org/common-1', 'prefix': 'stixCommon', 'children': {'Name': {'has_text': True, 'namespace': 'http://stix.mitre.org/common-1', 'prefix': 'stixCommon', 'children': None}}}, 'Time': {'has_text': False, 'namespace': 'http://stix.mitre.org/common-1', 'prefix': 'stixCommon', 'children': {'Produced_Time': {'has_text': True, 'namespace': 'http://cybox.mitre.org/common-2', 'prefix': 'cyboxCommon', 'children': None}}}}}}}, 'Role': {'has_text': True, 'namespace': 'http://stix.mitre.org/common-1', 'prefix': 'stixCommon', 'children': None}, 'Identity': {'has_text': False, 'namespace': 'http://stix.mitre.org/common-1', 'prefix': 'stixCommon', 'children': {'Name': {'has_text': True, 'namespace': 'http://stix.mitre.org/common-1', 'prefix': 'stixCommon', 'children': None}}}, 'Time': {'has_text': False, 'namespace': 'http://stix.mitre.org/common-1', 'prefix': 'stixCommon', 'children': {'Produced_Time': {'has_text': True, 'namespace': 'http://cybox.mitre.org/common-2', 'prefix': 'cyboxCommon', 'children': None}}}}}, 'Package_Intent': {'has_text': True, 'namespace': 'http://stix.mitre.org/stix-1', 'prefix': 'stix', 'children': None}, 'Description': {'has_text': True, 'namespace': 'http://stix.mitre.org/stix-1', 'prefix': 'stix', 'children': None}, 'Handling': {'has_text': False, 'namespace': 'http://stix.mitre.org/stix-1', 'prefix': 'stix', 'children': {'Marking': {'has_text': False, 'namespace': 'http://data-marking.mitre.org/Marking-1', 'prefix': 'marking', 'children': {'Controlled_Structure': {'has_text': True, 'namespace': 'http://data-marking.mitre.org/Marking-1', 'prefix': 'marking', 'children': None}, 'Marking_Structure': {'has_text': False, 'namespace': 'http://data-marking.mitre.org/Marking-1', 'prefix': 'marking', 'children': {'Terms_Of_Use': {'has_text': True, 'namespace': 'http://data-marking.mitre.org/extensions/MarkingStructure#Terms_Of_Use-1', 'prefix': 'terms', 'children': None}}}}}}}, 'Title': {'has_text': True, 'namespace': 'http://stix.mitre.org/stix-1', 'prefix': 'stix', 'children': None}}}, 'TTPs': {'has_text': False, 'namespace': 'http://stix.mitre.org/stix-1', 'prefix': 'stix', 'children': {'TTP': {'has_text': False, 'namespace': 'http://stix.mitre.org/stix-1', 'prefix': 'stix', 'children': {'Kill_Chain_Phases': {'has_text': False, 'namespace': 'http://stix.mitre.org/TTP-1', 'prefix': 'ttp', 'children': {'Kill_Chain_Phase': {'has_text': False, 'namespace': 'http://stix.mitre.org/common-1', 'prefix': 'stixCommon', 'children': None}}}, 'Intended_Effect': {'has_text': False, 'namespace': 'http://stix.mitre.org/TTP-1', 'prefix': 'ttp', 'children': {'Value': {'has_text': True, 'namespace': 'http://stix.mitre.org/common-1', 'prefix': 'stixCommon', 'children': None}}}, 'Resources': {'has_text': False, 'namespace': 'http://stix.mitre.org/TTP-1', 'prefix': 'ttp', 'children': {'Tools': {'has_text': False, 'namespace': 'http://stix.mitre.org/TTP-1', 'prefix': 'ttp', 'children': {'Tool': {'has_text': False, 'namespace': 'http://stix.mitre.org/TTP-1', 'prefix': 'ttp', 'children': {'Name': {'has_text': True, 'namespace': 'http://cybox.mitre.org/common-2', 'prefix': 'cyboxCommon', 'children': None}, 'Description': {'has_text': True, 'namespace': 'http://cybox.mitre.org/common-2', 'prefix': 'cyboxCommon', 'children': None}}}}}}}, 'Behavior': {'has_text': False, 'namespace': 'http://stix.mitre.org/TTP-1', 'prefix': 'ttp', 'children': {'Attack_Patterns': {'has_text': False, 'namespace': 'http://stix.mitre.org/TTP-1', 'prefix': 'ttp', 'children': {'Attack_Pattern': {'has_text': False, 'namespace': 'http://stix.mitre.org/TTP-1', 'prefix': 'ttp', 'children': {'Description': {'has_text': True, 'namespace': 'http://stix.mitre.org/TTP-1', 'prefix': 'ttp', 'children': None}}}}}}}, 'Title': {'has_text': True, 'namespace': 'http://stix.mitre.org/TTP-1', 'prefix': 'ttp', 'children': None}}}, 'Kill_Chains': {'has_text': False, 'namespace': 'http://stix.mitre.org/stix-1', 'prefix': 'stix', 'children': {'Kill_Chain': {'has_text': False, 'namespace': 'http://stix.mitre.org/common-1', 'prefix': 'stixCommon', 'children': {'Kill_Chain_Phase': {'has_text': False, 'namespace': 'http://stix.mitre.org/common-1', 'prefix': 'stixCommon', 'children': None}}}}}}}}}}}}

#h.register_message_handler(Stix111QueryHandler, name="Stix111QueryHandler")

