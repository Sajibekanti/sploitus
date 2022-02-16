import requests
import json
from sploitus.exploit import Exploit
import time


class Sploitus:
    HEALTHCHECK_URL = "https://sploitus.com/"
    SEARCH_URL = "https://sploitus.com/search"
    search_payload = {"type": "exploits", "sort": "default", "query": "windows", "title": True, "offset": 0}
    headers = {"User-Agent": "SploitusCmdlineAPI/1.0"}

    def __init__(self):
        if not self._health_check():
            raise Exception("Health check against sploitus.com failed, please try again later")

    def _health_check(self):
        health_check_resp = requests.get(self.HEALTHCHECK_URL, headers=self.headers)
        if health_check_resp.status_code != 200:
            return False
        return True

    def search(self, search_term, verbose=False):  # thread this to be quicker - we know the offset is always 10 at a time so can do this.
        search = self.search_payload
        search["query"] = search_term
        results = []
        retries = 0
        
        if verbose:
            self.search_payload["title"] = False

        while True:
            time.sleep(0.5)  # hopefully stops cloud flare
            if retries > 5:
                break

            search["offset"] = len(results)
            resp = requests.post(self.SEARCH_URL, headers=self.headers, json=search)
            
            try:
                resp = resp.json()
            except json.JSONDecodeError:
                time.sleep(0.5)
                retries += 1
                continue

            if isinstance(resp, list):
                time.sleep(0.5)
                retries += 1
                continue

            exploits = resp.get("exploits")
            if not exploits:
                retries += 1
                continue
            
            for exp in exploits:
                e = Exploit(    
                                        title=exp.get("title"),
                                        score=exp.get("score"),
                                        info_link=exp.get("href"),
                                        date=exp.get("published"),
                                        code=exp.get("source")    
                                    )

                # if e.code not in [ex.code for ex in results]:  
                results.append(e)
        return results

    def download_exploit(self, exploit):
        pass


def sort_exploits_by_score(exploits):
    if not isinstance(exploits, list):
        raise TypeError("exploits parameter was not a list of exploits")

    if not isinstance(exploits[0], Exploit):
        raise TypeError("exploits parameter was not a list of exploits")

    return sorted(exploits, key=lambda e: e.score, reverse=True)
    
