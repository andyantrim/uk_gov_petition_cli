from cache import Cache
from helpers import sort


class Report(object):
    def __init__(self, tid):
        self.id = tid

        self.cache = Cache(tid)

        mp_list = self.cache.get().get('data', {}).get('attributes', {}).get('signatures_by_constituency', [])
        self.mps = sort(mp_list)

        country_list = self.cache.get().get('data', {}).get('attributes', {}).get('signatures_by_country', [])
        self.countries = sort(country_list)

    def get_count(self):
        return self.cache.get().get("data", {}).get("attributes", {})['signature_count']

    def _search(self, query, queryset):
        result = []
        for item in queryset:
            for check in [str(i).lower() for i in item.values()]:
                if query.lower() in check:
                    result.append(item)
        return result

    def search_country(self, search):
        return self._search(search, self.countries)

    def search_mp(self, search):
        return self._search(search, self.mps)

    def print_countries(self, flist):
        print("|{:-^40}+{:-^40}+{:-^20}|".format("Name", "Code", "Signature"))
        for i in flist:
            name = i.get("name", "N/A")
            code = i.get("code", "NA")
            signature = i.get("signature_count", -1)
            try:
                print("|{:^40}|{:^40}|{:^20}|".format(name, code, signature))
            except:
                print("|{:^40}|{:^40}|{:^20}|".format("NA", "NA", "NA"))

    def print_mps(self, flist):
        print("|{:-^40}+{:-^40}+{:-^20}|".format("Name", "MP", "Signature"))
        for i in flist:
            name = i.get("name", "N/A")
            mp = i.get("mp", "NA")
            signature = i.get("signature_count", -1)
            try:
                print("|{:^40}|{:^40}|{:^20}|".format(name, mp, signature))
            except:
                print("|{:^40}+{:^40}+{:^20}|".format("NA", "NA", "NA"))
