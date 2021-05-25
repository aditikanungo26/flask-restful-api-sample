from .rulesmaster import saveruleset,getallRulesetWithVersion


def initialize_routes(api):
    api.add_resource(saveruleset, '/rest/api/rulesmaster/saveruleset')
    api.add_resource(getallRulesetWithVersion, '/rest/api/rulesmaster/getallRulesetWithVersion')
   