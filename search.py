from exa_py import Exa
from dotenv import load_dotenv
import os

load_dotenv()

class Search:
    def __init__(self):
        self.exa = Exa(api_key=os.getenv('EXA_API_KEY'))

    def search(self, query, results=10, include_domains=None, exclude_domains=None, include_text=None, exclude_text=None, moderation=False, autoprompt=True, type="neural"):
        return self.exa.search(query, num_results=results, type=type, moderation=moderation, use_autoprompt=autoprompt, include_domains=include_domains, exclude_domains=exclude_domains, include_text=include_text, exclude_text=exclude_text).results

    def get(self, url):
        return self.exa.get_contents(url).results
