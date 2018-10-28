import requests
import json


class Api():
    """API Client for stackoverflow"""

    site = "https://api.stackexchange.com/2.2/"

    def get_top_answer(self, question):
        # Vote-sorted questions
        method = "search?order=desc&sort=votes&intitle=\"{}\"&site=stackoverflow".format(question)

        questions_json = requests.get(self.site + method).json()
        items = questions_json["items"]
        ans_id = items[0]["accepted_answer_id"]

        ans_method = "answers/{}?order=desc&sort=activity&site=stackoverflow&filter=!9Z(-wzftf".format(ans_id)
        ans_json = requests.get(self.site + ans_method).json()

        return ans_json["items"][0]["body_markdown"]
